from django.shortcuts import render,redirect

def simple_middleware(get_response):

    def middleware(request):
        
        if '/a_panel/' in request.path:
            if not request.path == "/a_panel/auth_login/":
                if not request.user.is_superuser:
                    return redirect('/a_panel/auth_login/')
        
        if not('/' in request.path):
            if not request.user.is_authenticated:
                return redirect('/')
        
        if request.user.is_authenticated:
            if not (request.path == '/log/' or request.path == '/active/'):
                if request.user.is_authenticated:
                    if (hasattr(request.user, 'activecode')) and not request.user.activecode.status:
                        return redirect("/active/")
 

                



        response = get_response(request)

        return response

    return middleware