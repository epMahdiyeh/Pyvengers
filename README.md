# This Repository belongs to Pyvengers

Group Members :
Mahdiyeh, Saman, Ali, Alireza, Mahdi, Erfan

## Notes
### These Notes are to help you on the codes and exercises to understand better.

- `urls.py `: The only thing you should do is to append a path to urlpatterns.<br>
  `path(first_parameter:str, second_parameter: view_function)`<br>
  The first parameter is the path you want to show in url, the second one is the view method that you must call the
  related view, and 'name' field is for when you want to call or redirect that url in your templates.

  <br>

- `forms.py` : In this part, you should do some hard works. At first, you should import and inherit django ModelForm for
  your Form models. Then you have to define validation function in your form models. for validation function your
  function name should be like this pattern, at first the key word `clean` then your `field_name` for example to do some
  validations on address field you should set your function name like this: `def clean_address(self)`. Then in your
  function you should get the value of your target field by `cleaned_data` and do your process. If it's invalid you
  should raise
  validation error and if it's not return the value. Here's an example:
    ```
    def clean_name(self):  --> define validation function
      name = self.cleaned_data.get('name')  --> get the value of target key
      if len(name) < 4:  --> some conditions to check the validation
        raise forms.ValidationError('name is too short')  --> raise validation error with custom message
      return name
    ```

  <br>

- `templates` : In this part you should work on HTML files. There are some templates that you have to fill data in it with
  django template language (DTL). You should fill two parts in this question. The first is title that is a `static`
  value, and you just need to copy the text between two block
  quotes: `{% block title %}your title is here{% endblock title %}`. Then in next part you should call and show your
  data. Data is called from `views.py` for that template for example if you want to create product_list template and you
  want to get list of products from product model you can do this:
  ```
  {% for product in products %}
    {{ product }}
  {% endfor %}
  ```
  this code iterate through products and each time returns a product. Also, there are lots of methods and functions in
  DTL that you can use them in your project in case of need. Below we talk about some of them that used in this project:
  <br>
  `widthratio`: this method mostly use to change the ratio of boxes like div or something but in this exercise it used
  to multiply two variables. It gets three parameter, those are two variables and one ratio. for example this code
  multiply var1 to var2: `{% widthratio var1 1 var2 %}`. The point is that 3rd parameter has to be integer and if you
  want to multiply an int to a float you should set your float as first parameter
  like: `{% widthratio floatNum 1 intNum %}`.
  <br>
  `truncatechars`: This method is used to limit the string display and change the rest with `...`. Here's an example:
  `{{product.name|truncatechars:10}}` in this example we limit the size of display to 10 characters and the rest of
  string shows by `...`. The result of this method is something like this `Samsung ga...`, consider the name as 'Samsung
  galaxy note 10'.
  