text = input('Sisesta mingi tekst: ')

print(text,
      'on' if text == text[::-1] else
      'ei ole', 'palindroom')
