from django import template
from vegbasketapp.content.tools import get_entry_by_vg_id, get_vs_entry_by_id


register = template.Library()


@register.inclusion_tag('content/card_skel.html', takes_context=True)
def skeleton_card_vg(context, entry_id):
    entry = get_entry_by_vg_id(entry_id)
    return {"entry":entry}

@register.inclusion_tag('content/card_skel_533.html', takes_context=True)
def skeleton_card_vg_533(context, entry_id):
    entry = get_entry_by_vg_id(entry_id)
    return {"entry":entry}