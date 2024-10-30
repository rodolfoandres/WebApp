import reflex as rx

from .. import navigation
from ..ui.base import base_page

from . import form, state, model

def contact_entry_list_item(contact: model.ContactEntryModel):
    return rx.box(
        rx.heading(contact.first_name),
        rx.text(contact.message),
        padding='1em'
    )

# def foreach_callback(text):
#     return rx.box(rx.text(text))


def contact_entries_list_page() -> rx.Component:

    return base_page(
        rx.vstack(
            rx.heading("Contact Entries", size="5"),
            # rx.foreach(['abc', 'def', 'ghi'], foreach_callback),
            rx.foreach(state.ContactState.entries, contact_entry_list_item),
            spacing="5",
            align='center',
            min_height="85vh",
        )
    )


def contact_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Contact Us", size="9"),
            rx.cond(state.ContactState.did_submit, state.ContactState.thank_you, ""),
            rx.desktop_only(
                rx.box(
                    form.contact_form(),
                    width='50vw'
                ),
            ),
            rx.mobile_and_tablet(
                rx.box(
                    form.contact_form(),
                    width='85vw'
                ),
            ),
            spacing="5",
            justify="center",
            align='center',
            # text_align='center',
            min_height="85vh",
            id='my-child'
        )
    return base_page(my_child)