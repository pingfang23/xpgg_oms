from django.conf.urls import url, include
from . import views

# drf的router
from rest_framework.routers import DefaultRouter

# 实例化router对象
router = DefaultRouter()
# 通过router注册方式配置路由，快准狠
router.register(r'appreleaselist', views.AppReleaseListViewSet, base_name='appreleaselist')

urlpatterns = [
    # url(r'^$',views.index,name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^index_ajax$', views.index_ajax, name='index_ajax'),
    url(r'^login/$', views.do_login, name='login'),
    url(r'^logout/$', views.do_logout, name='logout'),
    url(r'^module_deploy/$', views.module_deploy, name='module_deploy'),
    url(r'^net_tool/$', views.net_tool, name='net_tool'),
    url(r'^minion_client_install/$', views.minion_client_install, name='minion_client_install'),
    url(r'^minion_manage/$', views.minion_manage, name='minion_manage'),
    url(r'^minion_manage_ajax/$', views.minion_manage_ajax, name='minion_manage_ajax'),
    url(r'^saltkey_manage/$', views.saltkey_manage, name='saltkey_manage'),
    url(r'^salt_key_global/$', views.salt_key_global, name='salt_key_global'),
    url(r'^salt_test_ping/$', views.salt_test_ping, name='salt_test_ping'),
    url(r'^salt_key_delete/$', views.salt_key_delete, name='salt_key_delete'),
    url(r'^salt_key_denied_delete/$', views.salt_key_denied_delete, name='salt_key_denied_delete'),
    url(r'^salt_key_accept/$', views.salt_key_accept, name='salt_key_accept'),
    url(r'^salt_key_reject/$', views.salt_key_reject, name='salt_key_reject'),
    url(r'^salt_cmd_manage/$', views.salt_cmd_manage, name='salt_cmd_manage'),
    url(r'^salt_cmd_manage_ajax/$', views.salt_cmd_manage_ajax, name='salt_cmd_manage_ajax'),
    url(r'^salt_exe/$', views.salt_exe, name='salt_exe'),
    url(r'^salt_exe_ajax/$', views.salt_exe_ajax, name='salt_exe_ajax'),
    url(r'^salt_tool/$', views.salt_tool, name='salt_tool'),
    url(r'^salt_tool_ajax/$', views.salt_tool_ajax, name='salt_tool_ajax'),
    url(r'^salt_file_manage/$', views.salt_file_manage, name='salt_file_manage'),
    url(r'^salt_file_manage_ajax/$', views.salt_file_manage_ajax, name='salt_file_manage_ajax'),
    url(r'^server_list/$', views.server_list, name='server_list'),
    url(r'^server_list_ajax/$', views.server_list_ajax, name='server_list_ajax'),
    url(r'^server_list_template_down/$', views.server_list_template_down, name='server_list_template_down'),
    url(r'^server_list_down/$', views.server_list_down, name='server_list_down'),
    url(r'^network_list/$', views.network_list, name='network_list'),
    url(r'^network_list_ajax/$', views.network_list_ajax, name='network_list_ajax'),
    url(r'^network_list_template_down/$', views.network_list_template_down, name='network_list_template_down'),
    url(r'^network_list_down/$', views.network_list_down, name='network_list_down'),
    url(r'^nginx_upstream/$', views.nginx_upstream, name='nginx_upstream'),
    url(r'^nginx_manage/$', views.nginx_manage, name='nginx_manage'),
    url(r'^nginx_conflist/$', views.nginx_conflist, name='nginx_conflist'),
    url(r'^nginx_reload/$', views.nginx_reload, name='nginx_reload'),
    url(r'^nginx_upstreamserver_add/$', views.nginx_upstreamserver_add, name='nginx_upstreamserver_add'),
    url(r'^app_release/$', views.app_release, name='app_release'),
    url(r'^app_release_test/$', views.app_release_test, name='app_release_test'),
    url(r'^app_release_ajax/$', views.app_release_ajax, name='app_release_ajax'),
    url(r'^app_group/$', views.app_group, name='app_group'),
    url(r'^app_group/app_group_members_manage/$', views.app_group_members_manage, name='app_group_members_manage'),
    url(r'^app_group_ajax/$', views.app_group_ajax, name='app_group_ajax'),
    url(r'^app_auth/$', views.app_auth, name='app_auth'),
    url(r'^app_auth/app_auth_app_manage/$', views.app_auth_app_manage, name='app_auth_app_manage'),
    url(r'^app_auth/app_auth_app_group_manage/$', views.app_auth_app_group_manage, name='app_auth_app_group_manage'),
    url(r'^app_auth_ajax/$', views.app_auth_ajax, name='app_auth_ajax'),
    url(r'^huawei_cdn/$', views.huawei_cdn, name='huawei_cdn'),
    url(r'^h5_issue/$', views.h5_issue, name='h5_issue'),
    url(r'^h5_svn_co/$', views.h5_svn_co, name='h5_svn_co'),
    url(r'^h5_svn_zip/$', views.h5_svn_zip, name='h5_svn_zip'),
    url(r'^h5_svn_push/$', views.h5_svn_push, name='h5_svn_push'),
    url(r'^h5_svn_unzip/$', views.h5_svn_unzip, name='h5_svn_unzip'),
    url(r'^h5_file/$', views.h5_file, name='h5_file'),
    # url(r'^nginx_add/$',views.nginx_add,name='nginx_add'),
    # url(r'^archive/$',views.archive,name='archive'),
    url(r'^test/$', views.server_list, name='test'),
    url(r'^api/', include(router.urls)),
]