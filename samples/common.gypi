{
  'target_defaults': {
    'configurations': [
      {
        'configuration_name': 'Debug',
        'conditions': [
          [ 'OS=="mac"', {
            'xcode_settings': {
              'COPY_PHASE_STRIP': 'NO',
              'GCC_OPTIMIZATION_LEVEL': '0',
            }
          }],
        ],
      },
      {
        'configuration_name': 'Release',
        'defines': [
          'NDEBUG',
        ],
        'conditions': [
          [ 'OS=="mac"', {
            'xcode_settings': {
              'DEAD_CODE_STRIPPING': 'YES',
            }
          }],
        ],
      },
    ],
  },
  'conditions': [
    [ 'OS=="mac"', {
      'target_defaults': {
        'xcode_settings': {
          'ALWAYS_SEARCH_USER_PATHS': 'NO',
          'GCC_C_LANGUAGE_STANDARD': 'c99',
          'GCC_CW_ASM_SYNTAX': 'NO',
          'GCC_DYNAMIC_NO_PIC': 'YES',
          'GCC_ENABLE_PASCAL_STRINGS': 'NO',
          'GCC_INLINES_ARE_PRIVATE_EXTERN': 'YES',
          'GCC_PRECOMPILE_PREFIX_HEADER': 'YES',
          'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES',
          # GCC_TREAT_WARNINGS_AS_ERRORS (-Wall) is temporarily disabled
          # during the bring-up.
          # 'GCC_TREAT_WARNINGS_AS_ERRORS': 'YES',
          'GCC_VERSION': '4.2',
          'GCC_WARN_ABOUT_MISSING_NEWLINE': 'YES',
          'MACOSX_DEPLOYMENT_TARGET': '10.5',
          'PREBINDING': 'NO',
          'SDKROOT': '$(DEVELOPER_SDK_DIR)/MacOSX10.5.sdk',
          'SYMROOT': '<(depth)/xcodebuild_gyp',
          'USE_HEADERMAP': 'NO',
          'WARNING_CFLAGS': '$(WARNING_CFLAGS) -Wall -Wendif-labels',
        },
      },
    }],
  ],
}