from ftw.upgrade import UpgradeStep


class InstallColorBox(UpgradeStep):

    def __call__(self):
        self.setup_install_profile(
            'profile-ftw.colorbox:default')
