'''
exploratory analysis
1. is one gender did significantly better in overall test than the other?
2. is one ethnic group better than others in overall test ? ANOVA 
3. is there a relation between parents level of education and maths score of a student ? (CORRELATION b/w categorical and continuous)
4. is there a relation between test preparation and maths score of a studentmathscore'] =dfsub['math score']
dfsub_dumy.drop(dfsub_dumy.index[len(dfsub_dumy)-1])
 ?
5. is any gender better at math than reading/ writing ?
6. does personal factors ( ethnicity, parents education ) have an effect on score ?
'''

# correlation  between nominal and continuous variable 
## age,size,color_head
## 4,50,black
## 9,100,blonde
## 12,120,brown
## 17,160,black
## 18,180,brown

df = pd.read_csv("StudentsPerformance.csv")
dfsub = pd.DataFrame(df['math score'])
dfsub['testprep']=df['test preparation course']
dfsub_dumy = pd.get_dummies(dfsub['testprep'])
dfsub_dumy['

grpbygen_eduparent = df.groupby(['gender','parental level of education'])['math score'].mean().reset_index()
fig,ax = plt.subplots(figsize=(12,5))
sns.barplot(x='parental level of education',y='math score',data=grpbygen_eduparent, hue='gender',ax=ax)


Groupby !
# If reset_index is not used the grouped column is returned as index or hierarchical index if multiple columns are selected.
df.groupby(['ID','Year']).mean().reset_index()
df.groupby(data['column']).function().reset_index()

#two categorical columns are grouped
df.groupby(['country','sex'])['suicides_no'].sum().reset_index().head()


