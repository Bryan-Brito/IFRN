
import speedtest

test = speedtest.Speedtest()

down = test.download()
rsDown = round(down)
fDown = int(rsDown / 1e+6)

upload = test.upload()
rsUp = round(upload)
fUp = int(rsUp / 1e+6)

print(f"Sua velocidade de Donwload é de: {fDown} mb/s")
print(f"Sua velocidade de Upload é de: {fUp} mb/s")
