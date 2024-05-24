from django.shortcuts import render, get_object_or_404
from .models import Service, Portfolio, PortfolioCategory, TeamMember, BlogPost, BlogCategory

def index(request):
    services = Service.objects.all()[:3]  # Fetching the first three services
    featured_portfolios = Portfolio.objects.all()[:3]  # Fetching the first three portfolio items
    team_members = TeamMember.objects.all()[:3]  # Fetching the first three team members
    recent_blog_posts = BlogPost.objects.order_by('-date')[:3]  # Fetching the three most recent blog posts
    
    context = {
        'services': services,
        'featured_portfolios': featured_portfolios,
        'team_members': team_members,
        'recent_blog_posts': recent_blog_posts
    }
    
    return render(request, 'index/index.html', context)
def about(request):
    return render(request, 'about/about.html')

def contact(request):
    return render(request, 'contact/contact.html')

def pricing(request):
    return render(request, 'pricing/table.html')
# Services
def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service.html', {'services': services})

def service_detail(request):
    return render(request, 'services/service_details.html')

# Portfolio
def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    categories = PortfolioCategory.objects.all()
    return render(request, 'portfolio/portfolio.html', {'portfolios': portfolios, 'categories': categories})

def portfolio_detail(request):
    return render(request, 'portfolio/portfolio_detail.html')

# Team Members
def team_list(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team/team.html', {'team_members': team_members})

def team_detail(request):
    
    return render(request, 'team/team_details.html')

# Blog
def blog(request):
    blog_posts = BlogPost.objects.all()
    categories = BlogCategory.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts, 'categories': categories})

def blog_detail(request):
    return render(request, 'blog/blog_detail.html')

from django.shortcuts import render

def blog_list(request):
    blogs = [
        {
            'image_url': 'assets/img/blog/blog-1.jpg',
            'date': '2020-06-27',
            'category': 'Business, Consulting',
            'title': 'Consulted admitting wooded is power acuteness',
            'details_url': 'blog-details.html',
        },
        {
            'image_url': 'assets/img/blog/blog-2.jpg',
            'date': '2021-04-30',
            'category': 'Business',
            'title': 'The 3 Most Effective Incentives for Employees',
            'details_url': 'blog-details.html',
        },
        # Add more blog entries here...
    ]
    return render(request, 'blog/blog.html', {'blogs': blogs})



def search(request):
    query = request.GET.get('q')
    services = Service.objects.filter(name__icontains=query) if query else Service.objects.none()
    portfolios = Portfolio.objects.filter(title__icontains=query) if query else Portfolio.objects.none()
    team_members = TeamMember.objects.filter(name__icontains=query) if query else TeamMember.objects.none()
    blog_posts = BlogPost.objects.filter(title__icontains=query) if query else BlogPost.objects.none()

    context = {
        'query': query,
        'services': services,
        'portfolios': portfolios,
        'team_members': team_members,
        'blog_posts': blog_posts,
    }
    
    return render(request, 'main/search_results.html', context)


