from flask import Blueprint,redirect,session, request
import Controller.sort_algorithm as sort
python_list_bp = Blueprint("python_list", __name__, template_folder="templates")


@python_list_bp.route("/sort_list", methods=["POST"])
def sort_list():
    if request.is_json:
        input_list = request.get_json().get('list')
    else:
        input_list = request.form.get('list').split(",")

    if not isinstance(input_list, list):
        session['announce'] = "Input must be a list"
        return redirect("/books")
    try:
        input_list = [int(item) for item in input_list]
        sorted_list = sort.bubble_sort(input_list)
        session['announce'] = f"Sorted list: {sorted_list}"
        return redirect("/books")
    except ValueError:
        session['announce'] = "You must enter valid number"
        return redirect("/books")


