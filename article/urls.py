# 简单来说就是Model存取数据，View决定需要调取哪些数据，而Template则负责将调取出的数据以合理的方式展现出来。

# 引入path
from django.urls import path
from article import views

# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    # path函数将url映射到视图
    path('article-list/', views.article_list, name='article_list'),
    # 文章详情
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    # 写文章
    path('article-create/', views.article_create, name='article_create'),
    # 安全删除文章
    # path('article-delete/<int:id>', views.article_delete, name='article_delete'),
    path('article-safe-delete/<int:id>', views.article_safe_delete, name='article_safe_delete'),
    # 更新文章
    path('article-updatee/<int:id>/', views.article_updatee, name='article_updatee'),
    #类视图新建文章
    path('create-view/', views.ArticleCreateView.as_view(), name='...'),
    #点赞 +1
    path('increase-likes/<int:id>', views.IncreaseLikesView.as_view(), name='increase_likes'),

]
