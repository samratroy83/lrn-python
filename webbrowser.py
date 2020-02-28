import webbrowser
google = raw_input('Google search:')
webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)