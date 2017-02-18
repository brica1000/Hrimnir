from thesite.models import Conglomerate, Product, Cert


"""Outsourcing compare_edits view"""
def new_old_color(info):
    try:
        message_0 = Product.objects.get(pk=info[0])
        message_1 = Product.objects.get(pk=info[1])
        message_type = 'product'
    except:  # If we can't find the entry in our products, then check the conglomerates.  We should make this more effecient one day..
        message_0 = Conglomerate.objects.get(pk=info[0])
        message_1 = Conglomerate.objects.get(pk=info[1])
        message_type = 'conglomerate'
    return message_0, message_1, message_type

def compare_fields(message_0, message_1):
    l = [ [x.name, x.category, x.text, x.sustainability, x.employees, x.num_stars] for x in [message_0, message_1]]  # create two lists
    fields = ['Name', 'Category', 'Text', 'Sustainability', 'Employees', 'Num Stars']
    style = []
    color = 'blue'
    for entry_0, entry_1 in zip(l[0],l[1]):
        if str(entry_0) != str(entry_1):
            style.append(color)
        else:
            style.append('no_style')
    return style, l[0], l[1], fields

def compare_with_colors_and_make_data_dic(info, data):  # info is from the two checkboxes, data is our dictionary to push to the template
    (message_1, message_0, message_type) = new_old_color(info)  # Swtich the order to control which info shows up on which side in compare_edits
    (style, l_left, l_right, fields) = compare_fields(message_0, message_1)
    data = { 'products': Product.objects.all(), 'conglomerates': Conglomerate.objects.all(),'info' : [],
             'message_0': "Nothing choosen", 'message_1': "", 'message_type': "", 'style': "", 'l_left': "", 'l_right': "",
             'zipped': "", 'zipped_repeat': ""}
    data['info'] = info
    data['message_0'] = message_0
    data['message_1'] = message_1
    data['message_type'] = message_type
    data['zipped'] = zip(style, l_left, l_right, fields)
    data['zipped_repeat'] = zip(style, l_left, l_right, fields)
    return data
