class TimerManager:

    def __init__(
        self,
        app,
        update_label_callback,
        timeout_callback
    ):

        self.app = app

        self.update_label_callback = update_label_callback

        self.timeout_callback = timeout_callback

        self.time_left = 15

        self.timer_running = False

        self.after_id = None

    # =========================================
    # Start Timer
    # =========================================
    def start_timer(self):

        self.stop_timer()

        self.time_left = 15

        self.timer_running = True

        self.update_timer()

    # =========================================
    # Stop Timer
    # =========================================
    def stop_timer(self):

        self.timer_running = False

        if self.after_id is not None:

            self.app.after_cancel(self.after_id)

            self.after_id = None

    # =========================================
    # Update Timer
    # =========================================
    def update_timer(self):

        if not self.timer_running:
            return

        self.update_label_callback(
            self.time_left
        )

        if self.time_left > 0:

            self.time_left -= 1

            self.after_id = self.app.after(
                1000,
                self.update_timer
            )

        else:

            self.timer_running = False

            self.timeout_callback()