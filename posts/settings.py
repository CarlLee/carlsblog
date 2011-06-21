from django.conf import settings
BLOG_TITLE = getattr(settings, 'BLOG_TITLE', 'Somebody\'s blog')
BLOG_SLOGAN = getattr(settings, 'BLOG_SLOGAN', 'Just another carlsblog...')
BLOG_HOMEPAGE = getattr(settings, 'BLOG_HOMEPAGE'
                        , {
                            'posts_per_page': 20,
                            'posts_digest_lines': 20,
                            })