import winreg

class LockScreenConfig:
    """A class to configure lock screen settings on Windows devices."""

    def __init__(self):
        self.registry_path = r"SOFTWARE\Policies\Microsoft\Windows\Personalization"

    def enable_lock_screen(self):
        """Enables the lock screen by setting the appropriate registry key."""
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.registry_path, 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key, "NoLockScreen", 0, winreg.REG_DWORD, 0)
            print("Lock screen enabled.")
        except Exception as e:
            print(f"Error enabling lock screen: {e}")

    def disable_lock_screen(self):
        """Disables the lock screen by setting the appropriate registry key."""
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.registry_path, 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key, "NoLockScreen", 0, winreg.REG_DWORD, 1)
            print("Lock screen disabled.")
        except Exception as e:
            print(f"Error disabling lock screen: {e}")

    def set_lock_screen_timeout(self, timeout: int):
        """Sets the lock screen timeout in seconds."""
        try:
            # Convert timeout from seconds to milliseconds
            timeout_ms = timeout * 1000
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.registry_path, 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key, "ScreenSaverTimeout", 0, winreg.REG_SZ, str(timeout_ms))
            print(f"Lock screen timeout set to {timeout} seconds.")
        except Exception as e:
            print(f"Error setting lock screen timeout: {e}")

if __name__ == "__main__":
    config = LockScreenConfig()
    config.enable_lock_screen()
    config.set_lock_screen_timeout(300)