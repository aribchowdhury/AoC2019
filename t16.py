x = "59754835304279095723667830764559994207668723615273907123832849523285892960990393495763064170399328763959561728553125232713663009161639789035331160605704223863754174835946381029543455581717775283582638013183215312822018348826709095340993876483418084566769957325454646682224309983510781204738662326823284208246064957584474684120465225052336374823382738788573365821572559301715471129142028462682986045997614184200503304763967364026464055684787169501819241361777789595715281841253470186857857671012867285957360755646446993278909888646724963166642032217322712337954157163771552371824741783496515778370667935574438315692768492954716331430001072240959235708"

output = [int(y) for y in x]
for phase in range(100):
    for i in range(len(output)):
        pattern = [0] * (i+1) + [1] * (i+1) + [0] * (i+1) + [-1] * (i+1)
        output[i] = int(str(sum([pattern[(j+1)%(len(pattern))]*output[j] for j in range(len(output))]))[-1])
    print("i") 
output = [str(x) for x in output]
print("".join(output))


x = x*10000
o = x[:7]
output = [int(y) for y in x][o:]
for i in range(100):
    s = sum(output)
    for j in range(len(output)):
        s -= output[j]
        output[j] = int(str(s+output[j])[-1])
print("".join(output[:8]))
#Just replace the inside of the string at the top with your input 
