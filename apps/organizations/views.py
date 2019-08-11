from django.shortcuts import render
from django.views.generic import View

from apps.organizations.models import CourseOrg, City

class OrgView(View):
    def get(self, request, *args, **kwargs):
        # 从数据库中获取数据
        all_org = CourseOrg.objects.all()
        all_city = City.objects.all()
        org_nums = CourseOrg.objects.count()
        return render(request, 'org-list.html',
                      {
                          'all_org': all_org,
                          'all_city': all_city,
                          'org_nums': org_nums
                      })
