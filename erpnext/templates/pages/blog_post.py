import frappe

def get_context(context):
    # Отримуємо значення параметра route з URL
    route = frappe.form_dict.get('route')
    
    # Отримуємо відповідний Blog Post з бази даних на основі route
    blog_posts = frappe.get_list(
        'Blog Post',
        filters={'route': ['like', f'%{route}%'], 'published': 1},
        fields=['*'])
    
    if not blog_posts:
        frappe.throw("Blog Post not found or not published", frappe.exceptions.DoesNotExistError)
    else:
        blog_post = blog_posts[0]

    # Додаємо дані поста до контексту для відображення
    context.blog_post = blog_post
