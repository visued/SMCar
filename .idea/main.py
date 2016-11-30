from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.utils import platform


class SmAgro(FloatLayout):
    def __init__(self, **kwargs):
        super(SmAgro, self).__init__(**kwargs)

class SMAgroApp(App):
    def __init__(self, **kwargs):
        super(SMAgroApp, self).__init__(**kwargs)

    # def call_App(self):
    #     if platform() == 'android':
    #
    #         PythonActivity = autoclass('org.renpy.android.PythonActivity')  # request the Kivy activity instance
    #         Intent = autoclass('android.content.Intent')  # get the Android Intend class
    #         intent = Intent()
    #         intent.setComponent(new ComponentName('com.navikey', 'com.navikey.seven_ways'))
    #         currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
    #         currentActivity.startActivity(intent)
    def call_App(self):
        if platform() == "android":
            from jnius import cast
            from jnius import autoclass

            PythonActivity = autoclass('org.renpy.android.PythonActivity')
            PythonActivity = autoclass('org.renpy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Context = autoclass('android.content.Context')
            activity = cast('android.app.Activity', PythonActivity.mActivity)

            # manager = autoclass('android.content.pm.PackageManager')
            # or:
            manager = activity.getPackageManager()

            intent = manager.getLaunchIntentForPackage("com.navikey.seven_ways")
            intent.addCategory(Intent.CATEGORY_LAUNCHER)

            activity.startActivity(intent)

    def build(self):
        return SmAgro()

if __name__ == '__main__':
    SMAgroApp().run()