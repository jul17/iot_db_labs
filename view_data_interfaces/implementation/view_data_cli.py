import view_data_interfaces.view_data as view_data_interface


class Cli(view_data_interface.ViewDataInterface):

    def view_data(self):
        print(self, flush=True)
        pass