'''@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def fpassword(request):
    form = FpasswordForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data["email"]
        if function_checkemail(email):
            form.save(from_email='blabla@blabla.com',
                      email_template_name='registration/password_reset_email.html', request=request)
            print "EMAIL SENT"
        else:
            print "UNKNOWN EMAIL ADRESS"

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def fpassword(request):
    form = FpasswordForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data["email"]
        if function_checkemail(email):
            form.save(from_email='blabla@blabla.com',
                      email_template_name='registration/password_reset_email.html')
            print
            "EMAIL SENT"
        else:
            print
            "UNKNOWN EMAIL ADRESS"'''