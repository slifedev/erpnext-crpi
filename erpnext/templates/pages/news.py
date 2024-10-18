import frappe
from frappe.website.utils import cleanup_page_name

def get_context(context):
    # Отримати всі опубліковані блог-пости
    blog_posts = frappe.get_all('Blog Post', 
        filters={'published': 1}, 
        fields=['title', 'route', 'published_on', 'blog_intro', 'meta_image', 'blog_category', 'blogger'],
        order_by="published_on desc"
    )


    for post in blog_posts:
        try:
            post['route'] =  post.get('route').split('/')[2]
        except Exception as e:
            post['route'] = ''
            print(str(e))

        try:
            bloggerData = frappe.db.get_value(
                'Blogger',
                post.blogger,
                ['full_name', 'avatar'])
            post['blogger_full_name'] = bloggerData[0] if bloggerData[0] else 'Unknown blogger'
            
        except Exception as e:
            print("Error fetching blogger:", str(e))
            post['blogger_full_name'] = 'Unknown Blogger'
            post['blogger_photo'] = ''
            

    # Додати блог-пости в контекст для рендерингу в шаблоні
    context.blog_posts = blog_posts
    
