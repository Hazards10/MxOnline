from django.shortcuts import render
from django.views.generic import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger  #分页插件

from apps.organizations.models import CourseOrg, City


class OrgView(View):
    def get(self, request, *args, **kwargs):
        # 从数据库中获取数据
        all_org = CourseOrg.objects.all()
        all_city = City.objects.all()
        org_nums = CourseOrg.objects.count()
        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_org, per_page=5, request=request)
        orgs = p.page(page)
        return render(request, 'org-list.html',
                      {
                          'all_org': orgs,
                          'all_city': all_city,
                          'org_nums': org_nums,
                      })
