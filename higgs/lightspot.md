#### Xiang Wang @ 2017-05-14 19:19:01


* 装饰器的合理使用，避免大量冗余代码

```
    def log_error(f):
        """对所有的错误进行错误，并记录不正常的日志"""
        def fin(*args, **kw):
            try:
                return f(*args, **kw)
            except ObjectDoesNotExist:
                return json_resp(code=404)
            except AssertionError as e:
                return json_resp(code=400, msg_extend=e.args[0] if e.args else "")
            ... 其他一些错误处理...
            except Exception as e:
                error_log = logging.getLogger('error')
                error_log.error(traceback.format_exc())
                etype, value, tb = sys.exc_info()
                tb_view = tb.tb_next
                if tb_view:
                    filename, lineno, functionname, code = traceback.extract_tb(tb_view)[0]
                    text = "{error_msg} in file {filename} on line {lineno}".format(
                        error_msg=repr(e),
                        filename=filename,
                        lineno=lineno,
                    )
                else:
                    text = e
                log.error(text)
                return json_resp(code=500)
    
        return update_wrapper(fin, f)
    
    
    def captcha_verify(f):
        """给django的view使用的验证码的装饰器"""
        def fin(*args, **kw):
            request = args[1]
            if request.method == "GET":
                request_data = request.query_params
            elif request.method == "POST":
                request_data = request.POST
            gt = GeetestLib(GEETEST_ID, GEETEST_KEY)
            challenge = request_data.get(gt.FN_CHALLENGE, '')
            validate = request_data.get(gt.FN_VALIDATE, '')
            seccode = request_data.get(gt.FN_SECCODE, '')
            result = gt.success_validate(challenge, validate, seccode)
            if not result:  # 正常使用的情况下，都不会出现这个情况的。
                log.error("有人用脚本来访问")
                return json_resp(code=403, msg_extend="请完成验证码校验")
            else:
                return f(*args, **kw)
        return update_wrapper(fin, f)
```


* 在公司已有的用户体系上实现了一套oauth认证体系

* 合理创建类，用于时间处理
```
    @python_2_unicode_compatible
    class Week(object):
        """
            默认设置每年的第一个周一开始为的第一周
            默认设置每周从周一开始，周日结束
        """
    
        def __init__(self, year, week):
            """
                year: 年份
                week: 第几周
            """
            assert 1970 < year < 9999
            assert 1 <= week <= 53
            self.year = year
            self.week = week
    
        @classmethod
        def create_from_date(cls, date_obj):
            """
                date: datetime.date
                example: week = Week.create_from_date(date(2016, 9, 18))
            """
            year = date_obj.year
            week = int(date_obj.strftime('%W'))
            if week == 0:
                date_obj = date(year - 1, 12, 31)
                return cls.create_from_date(date_obj=date_obj)
            week_obj = cls(year=date_obj.year, week=week)
            return week_obj
    
        @property
        def startdate(self):
            new_years_day = date(year=self.year, month=1, day=1)
            startdate = new_years_day + \
                datetime.timedelta(days=(7 - new_years_day.weekday()) % 7) + \
                datetime.timedelta(days=(self.week - 1) * 7)
            return startdate
    
        @property
        def startdatetime(self):
            return datetime.datetime.strptime(
                self.startdate.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    
        @property
        def enddate(self):
            enddate = self.startdate + datetime.timedelta(days=6)
            return enddate
    
        @property
        def enddatetime(self):
            return datetime.datetime.strptime(
                self.enddate.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S") +\
                datetime.timedelta(days=0, seconds=3600 * 24)
    
        def next_week(self):
            return Week.create_from_date(self.startdate + datetime.timedelta(days=7))
    
        def get_year_week(self):
            week = "%d%02d" % (self.year, self.week)
            return week
    
        def __str__(self):
            start = normal_unicode(self.startdate.strftime("%m月%d日"))
            end = normal_unicode(self.enddate.strftime("%m月%d日"))
            return u"{0}年第{1}周: {2}~{3}".format(self.year, self.week, start, end)
    
        def get_next_week(self):
            """返回下一个星期的instance"""
            return Week.create_from_date(
                self.startdate + datetime.timedelta(days=7))
    
        def get_previous_week(self):
            """返回上一个星期的instance"""
            return Week.create_from_date(
                self.startdate - datetime.timedelta(days=7))
    
        @classmethod
        def thisweek(self):
            return self.create_from_date(datetime.date.today())
    
        def __add__(self, integer):
            """返回n周后的星期"""
            return Week.create_from_date(
                self.startdate + datetime.timedelta(days=7*integer))
    
        def __sub_integer__(self, integer):
            """返回n周前的星期"""
            return Week.create_from_date(
                self.startdate - datetime.timedelta(days=7*integer))
    
        def __gt__(self, week):
            if self.year > week.year:
                return True
            elif self.year < week.year:
                return False
            else: return self.week > week.week
    
        def __sub__(self, week):
            """计算两个星期之间差几个星期"""
            if isinstance(week, int):
                return self.__sub_integer__(week)
            return (self.startdate - week.startdate).days/7
```

* 利用类，条理清楚地实现递归循环
```
    class Extend(object):
        def __init__(self, name, extend, user_paper, positive=1, parent=None):
            """
                因为要递归，所以把extend写成了一个对象
                注意: extend只适用于第二层开始的extend。第一层的"0", "1"请不要传入
            """
            self.extend = extend
            self.name = name
            self.parent = parent
            self.positive = positive
            self.user_paper=user_paper
            self.validate()
            if self.parent is None:
                self.path = self.name
            else:
                self.path = "%s/%s" % (self.parent.path, self.name)
            # XXX 使用缓存字段来存储headers。考虑到extend最多五层，暂时不做
            # self.headers = None

        def validate(self):
            """
                校验数据格式
                前期，有错先暴露出来。把问题找到。数据格式必须正确
            """
            assert isinstance(self.name, six.string_types), "extend的维度名称必须是字符串"
            ...其他数据校验...

        def get_headers(self):
            """
                输出extend的headers: ['父维度/符合', '父维度/子维度1/符合', '父维度/子维度1/孙维度1/符合', '父维度/子维度2/符合']
            """
            ...获取header...

        def get_children(self):
            """
                获取extend的子维度
            """
            children = []
            for key in self.extend:
                if key in ['score', 'total', 'full_score']:
                    continue
                else:
                    extend = Extend(name=key, extend=self.extend[key],
                                    user_paper=self.user_paper,
                                    positive=self.positive, parent=self)
                    children.append(extend)
            return children

        def get_score(self):
            """
                得到extend的score
            """
            # XXX score也可以做缓存
            score = self.extend.get('score', 0)
            for child in self.get_children():
                score += child.get_score()
            return score

        def get_adjustmented_score(self):
            """
                获取归一化的score，如果归一化为False，就直接传出原始score
            """
            children = self.get_children()
            result_desc = json.loads(self.user_paper.paper.result_desc)

            if result_desc.get('fmt_score_flag', False) is False:  # 不要归一化
                return self.get_score()
            else:
                assert 'full_score' in self.extend, "叶子维度没有总分"
                assert isinstance(self.extend['full_score'], int)
                perfect_score = int(result_desc['range'])
                return self.get_score()*1.0/self.extend['full_score']*perfect_score

        def get_data(self):
            """
                得到extend的数据 {
                    "父维度/符合": 5,
                    "父维度/子维度1/符合": 1,
                    "父维度/子维度1/孙维度1/符合": 2,
                    "父维度/子维度2/符合": 1,
                }
                可以嵌套，但是这样外层get_data也要递归了。为了生成csv方便，直接平铺开来
            """
            result = {}
            # 把自己的数据放入结果
            if self.positive == 1:
                header = "%s/符合" % self.path
            elif self.positive == 0:
                header = "%s/不符合" % self.path
            children = self.get_children()
            if len(children)==0:  # 叶子维度，获取归一化的分数
                result[header] = self.get_adjustmented_score()
            else:
                result[header] = self.get_score()
                for child in self.get_children():
                    result.update(child.get_data())
            return result
```

* 合理规划功能模块区分，非常方便之后功能的拓展与修改
```
class DailyPaperDetailAPIView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,
                          permissions.DailyPaperPermission)
    serializer_class = serializers.DailyPaperDetailGetSerializer
    model = models.DailyPaper
    queryset = models.DailyPaper.objects.all()
    http_method_names = ['get', 'patch', 'delete']

    class DailyPaperFilterSet(django_filters.rest_framework.FilterSet):
        before = django_filters.DateFilter(name="date", lookup_expr="lt")

        class Meta:
            model = models.DailyPaper
            fields = ["status", "user", "date", "id", "before"]

    filter_class = DailyPaperFilterSet

    def get_queryset(self):
        ...根据自己的用户等级，先过滤能访问的数据库数据...
        queryset = self.queryset
        if 'user' in self.request.query_params:  # 不看自己的日报就要过滤掉草稿
            # XXX target可以储存在self里面。这样就不用和permission重复查找了
            # 不过反正django 和 mysql会有缓存机制，影响不大
            target_user = User.objects.get(id=self.request.query_params['user'])
            if target_user != self.request.user:
                queryset = queryset.exclude(status=1)
        return queryset

    def get_object(self):
        queryset = self.filter_class(self.request.query_params, self.get_queryset()).qs
        if self.request.method == 'PATCH':
            if 'id' in self.request.data:
                queryset = queryset.filter(id=self.request.data.get('id'))

        if self.request.method == 'GET':  # 如果有before，那就需要返回最近的一份日报
            if 'before' in self.request.query_params:
                queryset = queryset.order_by('-date')[0:1]

        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        log.info("权限认证成功")
        return obj

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.frozen is True:
            return Response(json.loads(instance.extra))
        else:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

    @log_error
    def get(self, request, *args, **kwargs):
        """获取日报的详情"""
        log.info("获取日报详情")
        try:
            response = self.retrieve(request, *args, **kwargs)
        except MultipleObjectsReturned as e:
            return json_resp(code=400, msg_extend="请输入更详细的筛选条件")
        return json_resp(code=response.status_code, data=response.data)

    def get_serializer(self, *args, **kwargs):

        # 自己可以全部修改，领导只能修改状态
        instance = args[0]
        if self.request.method == 'GET':
            serializer_class = serializers.DailyPaperDetailGetSerializer
        elif self.request.method == 'PATCH':
            if instance.user == self.request.user:
                suffix = ""
            else:
                suffix = "ForLeader"
            serializer_class_name = "DailyPaperPatchSerializer%d%s" % (
                instance.status, suffix)
            log.info("使用序列化类: %s" % serializer_class_name)
            serializer_class = getattr(serializers, serializer_class_name)
            log.info("只需的fields有: %s" % serializer_class.Meta.read_only_fields)
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    @log_error
    def patch(self, request, *args, **kwargs):
        """
        修改日报的信息
        """
        log.info("修改日报详情")
        response = super(DailyPaperDetailAPIView, self).patch(
            request, *args, **kwargs)
        return json_resp(code=response.status_code, data=response.data)

    @log_error
    def delete(self, request, *args, **kwargs):
        # TODO 上线时删除该接口
        """
        TODO 删除日报。给测试用，上线删除
        """
        instance_id = request.data.get('id', None)
        if instance_id is None:
            raise ValidationError({'id': ['id是必填项']})
        # instance = self.get_queryset().get(id=instance_id)
        instance = self.queryset.get(id=instance_id)
        # TODO 现在允许任何人删除日报，方便前端测试。
        # self.check_object_permissions(self.request, instance)
        instance.delete()
        return json_resp(code=201)
```
