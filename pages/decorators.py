from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def login_required(function=None, redirect_field_name='labvltop', login_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated,
        login_url=login_url,
        redirect_field_name='labvltop'
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def staff_required(view_func=None, redirect_field_name='labvltop', message='error'):
    # """
    # Decorator for views that checks that the user is logged in and is
    # staff, displaying message if provided.
    # """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff and u.is_authenticated,
        login_url='loly_login',
        redirect_field_name='labvltop',
        # message=message
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'Department head':
			return redirect('user-page')

		if group == 'Quality manager':
			return view_func(request, *args, **kwargs)

	return wrapper_function