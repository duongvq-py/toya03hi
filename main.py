#region import bailam_f
from s00_bailam import hi as bailam_f
#endregion import bailam_f

#region chambai
from s02_chambai import chambai

#region testkey_list
testcase_list = [
    {
        'tc_name': 'tc0',
        'input': {
            'name': 'Mom'
        },
        'output': 'Hi Mom!'
    },
    {
        'tc_name': 'tc3',
        'input': ['Mom'],
        'output': 'Hi Mom!'
    },
    {
        'tc_name': 'tc4',
        'input': {
            'name': ''
        },
        'output': 'Hi!'
    },
    {
        'tc_name': 'tc1',
        'input': {},
        'output': 'Hi!'
    },
    {
        'tc_name': 'tc2',
        'input': {
            'name': None
        },
        'output': 'Hi!'
    },
    {
        'tc_name': 'tckho1',
        'input': ['Mom', 'Dad'],
        'output': 'Hi Mom, and Dad!'
    },
    {
        'tc_name': 'tckho2',
        'input': ['A', 'B', 'C'],
        'output': 'Hi A, B, and C!'
    },
    {
        'tc_name': 'tckho3',
        'input': ['1', '22', '333', '4444'],
        'output': 'Hi 1, 22, 333, and 4444!'
    },
]
#endregion testkey_list

ketqua_list = []
for tc in testcase_list:  # tc aka testcase
  INP_name = tc['input']
  tc_score, o_BAILAM = chambai(tc, bailam_f)

  ketqua_list.append({
      'tc_name': tc['tc_name'],
      'tc_score': tc_score,
      'o_TESTCASE': tc['output'],
      'o_BAILAM': o_BAILAM,
  })
#endregion chambai

#region in ketqua
print('---ketqua chitiet')
for kq in ketqua_list:
  print(f'''
{kq['tc_name']} {kq['tc_score']}
o_TESTCASE = {kq['o_TESTCASE']}
o_BAILAM   = {kq['o_BAILAM']}
  '''.strip() + '\n')

print('\n---ketqua')

for kq in ketqua_list:
  print(f'''{kq['tc_name']} {kq['tc_score']}''')
#endregion in ketqua
