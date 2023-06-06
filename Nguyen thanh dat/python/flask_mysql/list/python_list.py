from flask import Blueprint,redirect,session, request

python_list_bp = Blueprint("python_list", __name__, template_folder="templates")

@python_list_bp.route("/sort_list", methods=["POST"])
def sort_list():
    try:
        if request.is_json:
            input_list = request.get_json().get('list')
        else:
            input_list = request.form.get('list').split(",")

        if not isinstance(input_list, list):
            session['announce'] = "Input must be a list"
            return redirect("/books")
        try:
            input_list = [int(item) for item in input_list]
            for item in input_list:
                if not isinstance(item, int):
                    session['announce'] = f"Input must be an integer number{input_list}"
                    return redirect("/books")

            sorted_list = bubble_sort(input_list)
            session['announce'] = f"Sorted list: {sorted_list}"
            return redirect("/books")
        except ValueError:
            session['announce'] = "You must enter valid number"
            return redirect("/books")

    except Exception as e:
        return 'Error: ' + str(e)

def bubble_sort(list):
    for i in range(0, len(list)):
        for j in range(0, len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list