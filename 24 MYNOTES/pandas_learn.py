
poke[poke.loc[row,col]]
poke[poke.loc[:,'Name'] == 'SomeName']
poke[poke.loc[:,'Name'].isin(['SomeName','NameTwo'])]
poke[poke.loc[:,'Name'].isin(['Pikachu', 'Bulbasaur'])]

only_common = poke[poke['Legendary'==FALSE]]

# Subset of pokemon that don't contain 'Mega' in their name.

no_mega = poke[~poke['Name'].str.contains('Mega')]

Removing mega wasn't enough. Let's consider all pokemon with same number as duplicates, drop them and keep only the first one.

nodup_poke = poke.drop_duplicates('Number',keep='first', inplace = False )
# nodup_poke will have indexes borrowed from original data so it will not be aliged
#  Reindex the dataframe, so the first index is 0 and the last is n-1

nodup_poke.reset_index(inplace= True,drop = True)

# how many unique pokemons are there in the remaining data 
len(nodup_poke['Number'].unique())

# which pokemon is strongest and weakest
strongest_type = nodup_poke[['type1','total']].grouby(nodup_poke['Type1']).sort_values( by =   'Total')    


