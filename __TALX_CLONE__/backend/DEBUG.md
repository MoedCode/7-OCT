# url
```s
http://127.0.0.1:8000/api/like/
```
# output
```sh
mohamed@DESKTOP-S296B4S /mnt/c/Users/Active/Desktop/Coding/Short_Specializations/Portfolio_project/Xtwittes/__TALX_CLONE__/backend
 % ./manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 20, 2024 - 16:12:18
Django version 4.2.10, using settings 'backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Method Not Allowed: /api/like/
[20/Jul/2024 16:12:23] "GET /api/like/ HTTP/1.1" 405 6834
Internal Server Error: /api/like/
Traceback (most recent call last):
  File "/home/mohamed/.local/lib/python3.8/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
  File "/home/mohamed/.local/lib/python3.8/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/mohamed/.local/lib/python3.8/site-packages/django/views/decorators/csrf.py", line 56, in wrapper_view
    return view_func(*args, **kwargs)
  File "/home/mohamed/.local/lib/python3.8/site-packages/django/views/generic/base.py", line 104, in view
    return self.dispatch(request, *args, **kwargs)
  File "/home/mohamed/.local/lib/python3.8/site-packages/rest_framework/views.py", line 509, in dispatch
    response = self.handle_exception(exc)
  File "/home/mohamed/.local/lib/python3.8/site-packages/rest_framework/views.py", line 469, in handle_exception
    self.raise_uncaught_exception(exc)
  File "/home/mohamed/.local/lib/python3.8/site-packages/rest_framework/views.py", line 480, in raise_uncaught_exception
    raise exc
  File "/home/mohamed/.local/lib/python3.8/site-packages/rest_framework/views.py", line 506, in dispatch
    response = handler(request, *args, **kwargs)
  File "/mnt/c/Users/Active/Desktop/Coding/Short_Specializations/Portfolio_project/Xtwittes/__TALX_CLONE__/backend/api/views.py", line 248, in post
    if user_id in comment.dislikes:
TypeError: argument of type 'ManyRelatedManager' is not iterable
[20/Jul/2024 16:12:35] "POST /api/like/ HTTP/1.1" 500 91275

```
code
```py
class Like(APIView):
    def get(self, request):return Response(use_POST,status=S405)

    def post(self, request):
        token = request.headers.get('Authorization') or request.data["token"] or None
        username = auth.get_by(token=token) or None
        if not username:
            return Response(status=S401)
        data = request.data or None
        if not data:
            return Response({"Error": "Request data missing"},
            status=S400)

        user_id = Users.objects.filter(username=username).first().ID

        comment_data = data.get("comment") or None
        post_data = data.get("post") or None

        if not comment_data and not post_data:
            msg = "Comment or post data also required"
            return Response({"Error": msg}, status=S400)
        if comment_data:
            ID = comment_data.get("ID") or None
            action = comment_data.get("action") or None
            if not ID or not action:
                return Response({"Error":"ID, action required"},status=S400)

            comment = Comment.objects.filter(ID=ID).first()
            if action == "like":
                if user_id in comment.dislikes:
                    comment.dislikes.remove(user_id)
                comment.likes.append(user_id)
            if action == "dislike":
                if user_id in comment.likes:
                    comment.likes.remove(user_id)
                comment.dislikes.append(user_id)


        return Response({"detail": f"Like processed successfully {comment.likes}"},
        status=S200)

```
request
```json
{
"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Ikt5b2tvIiwiZXhwIjoxNzIxMTk0MjcxfQ.wlkL7OrId4K_yO7dBO2HRwjBQwC22rS5gf7H2sAEhrk",

"comment": {

    "ID": "7fd3b1a4-340f-4d60-8d6e-60838c7981ea",
    "action":"like"
    }
}
```