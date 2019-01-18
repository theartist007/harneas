def time_diff(time_later, time_earlier):
	start_index=time_earlier.index('T')
	end_index=time_earlier.index('Z')

	time_earlier=time_earlier[start_index+1:end_index]

	start_index=time_later.index('T')
	end_index=time_later.index('Z')

	time_later=time_later[start_index+1:end_index]
	
	time_earlier=time_earlier.split(":")
	time_later=time_later.split(":")

	for (i, value) in enumerate(time_earlier):
		time_earlier[i]=int(value)

	for (i, value) in enumerate(time_later):
		time_later[i]=int(value)

	time_earlier.reverse()
	time_later.reverse()

	time_elapsed=[0, 0, 0];
	
	for i in range(3):
		diff=time_later[i]-time_earlier[i]
		if(diff<0 and i!=2):
			diff=diff+60
			time_later[i+1]=time_later[i+1]-1
		elif(diff<0 and i==2):
			diff=diff+24

		time_elapsed[i]=diff

	return 10+time_elapsed[0] + time_elapsed[1]*60 + time_elapsed[2]*3600



import json

fileptr = open("DS1.json")
data=json.loads(fileptr.read())

base_time=-1;
with open("data1.csv", "w") as target:
	target.write(f'P,')
	target.write(f'S,')
	target.write(f'T,')
	target.write(f'S^2')
	target.write(f'PxS')
	target.write(f'Px(S^2)')
	target.write(f'(P^2) xS')
	target.write(f'(P^2) x (S^2)')
	target.write(f'Temp\n')

	for dic in data:
		pres=dic["Pressure"]
		rpm=dic["RPM"]
		time_current=dic["_time"]
		temp=dic["Temperature"]
			
		if(base_time==-1):
			base_time=time_current

		time_elapsed=time_diff(time_current, base_time)


		target.write(f'{pres},')
		target.write(f'{rpm},')
		target.write(f'{time_elapsed},')
		target.write(f'{rpm*rpm},')
		target.write(f'{pres*rpm},')
		target.write(f'{pres*rpm*rpm},')
		target.write(f'{pres*pres*rpm},')
		target.write(f'{pres*pres*rpm*rpm},')
		target.write(f'{temp}\n')

fileptr = open("DS2.json")
data=json.loads(fileptr.read())

base_time=-1
with open("data2.csv", "w") as target:
	
	target.write(f'P,')
	target.write(f'S,')
	target.write(f'T,')
	target.write(f'S^2')
	target.write(f'PxS')
	target.write(f'Px(S^2)')
	target.write(f'P^2 xS')
	target.write(f'P^2 x S^2')
	target.write(f'Temp\n')

	for dic in data:

		pres=dic["Pressure"]
		rpm=dic["RPM"]
		time_current=dic["_time"]
		temp=dic["Temperature"]
			
		if(base_time==-1):
			base_time=time_current

		time_elapsed=time_diff(time_current, base_time)


		target.write(f'{pres},')
		target.write(f'{rpm},')
		target.write(f'{time_elapsed},')
		target.write(f'{rpm*rpm},')
		target.write(f'{pres*rpm},')
		target.write(f'{pres*rpm*rpm},')
		target.write(f'{pres*pres*rpm},')
		target.write(f'{pres*pres*rpm*rpm},')
		target.write(f'{temp}\n')
