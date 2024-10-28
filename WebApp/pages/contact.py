import asyncio
import reflex as rx

from ..ui.base import base_page
from .. import navigation

class ContactState(rx.State):
    form_data: dict = {}
    did_submit: bool = False
    timeleft: int = 5

    @rx.var
    def timeleft_label(self):
        if self.timeleft < 1:
            return "No time left"
        return f"{self.timeleft} seconds"

    @rx.var
    def thank_you(self):
        first_name = self.form_data.get("first_name") or ""
        return f"Thank you {first_name}".strip()+"!"

    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data
        self.did_submit = True
        yield
        await asyncio.sleep(2)
        self.did_submit = False
        yield
    
    async def start_timer(selft):
        while selft.timeleft > 0:
            await asyncio.sleep(1)
            selft.timeleft -= 1
            yield


@rx.page(
        on_load=ContactState.start_timer,
        route=navigation.routes.CONTACT_US_ROUTE)
def contact_page() -> rx.Component:
    my_form = rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        placeholder="First Name",
                        name="first_name",
                        type="text",
                        width='100%',
                        required=True
                    ),
                    rx.input(
                        placeholder="Last Name",
                        name="last_name",
                        type="text",
                        width='100%',
                    ),
                    width='100%'
                ),
                rx.input(
                    placeholder="Your email",
                    name='email',
                    type='email',
                    width='100%',
                ),
                rx.text_area(
                    name='message',
                    placeholder='Your Message',
                    width='100%',
                    required=True
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
    )
    
    my_child = rx.vstack(
            rx.heading("Contact Us", size="9"),
            rx.text(ContactState.timeleft_label),
            rx.cond(ContactState.did_submit, ContactState.thank_you, ""),
            rx.desktop_only(
                rx.box(
                    my_form,
                    width='50vw'
                ),
            ),
            rx.mobile_and_tablet(
                rx.box(
                    my_form,
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