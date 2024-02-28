from setuptools import setup

setup(
    name='stellar-horizon-wallpaper',
    options={
        'build_apps': {
            # Build stellar-horizon-wallpaper as GUI application
            'gui_apps': {
                'stellar-horizon-wallpaper': 'scene_builder.py',
            },
            # Output logging
            'log_filename': '$USER_APPDATA/stellar-horizon-wallpaper/output.log',
            'log_append': False,
            # Files included with the distribution
            'include_patterns': [
                '**/*.png',
                '**/*.jpg',
                '**/*.egg',
            ],
            # Included plugins
            'plugins': [
                'pandagl',
                'p3openal_audio',
            ],
        }
    }
)