import frappe
from frappe.website.utils import cleanup_page_name

def get_context(context):
    # Отримати всі опубліковані блог-пости
    blog_posts = frappe.get_all('Blog Post', 
        filters={'published': 1}, 
        fields=['title', 'route', 'published_on', 'blog_intro', 'meta_image', 'blog_category'],
        order_by="published_on desc"
    )
    for post in blog_posts:
        try:
            post['route'] =  post.get('route').split('/')[2]
        except Exception as e:
            post['route'] = ''
            print(str(e))

    # Додати блог-пости в контекст для рендерингу в шаблоні
    context.blog_posts = blog_posts
    
    # Ви також можете додати інші контексти, наприклад, мета-заголовки чи додаткову інформацію
    context.title = "News and Blog Posts"
