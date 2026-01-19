followers = {'Hamid','Rayan','Qasim'}
following = {'Hamid','Shaista','Qasim','Rayan','Ali','ronaldo'}

imposters = following - followers
mutuals = following & followers
total_account = followers | following


print(f'imposters = {imposters} ')
print(f'mutuals = {mutuals} ')
print(f'total_account = {total_account} ')
