from thesite.models import Conglomerate, Product, Cert




def new_old_color(info):
    try:
        message_0 = Product.objects.get(pk=info[0])
        message_1 = Product.objects.get(pk=info[1])
    except:  # If we can't find the entry in our products, then check the conglomerates.  We should make this more effecient one day..
        message_0 = Conglomerate.objects.get(pk=info[0])
        message_1 = Conglomerate.objects.get(pk=info[1])
    return message_0, message_1


def compare_fields(message_0, message_1):
    l = [ [x.name, x.text, x.approved_edit] for x in [message_0, message_1]]  # create two lists
    style = []
    color = 'blue'
    for entry_0, entry_1 in zip(l[0],l[1]):
        if str(entry_0) != str(entry_1):
            style.append(color)
        else:
            style.append('no_style')
    return style, l[0], l[1]
