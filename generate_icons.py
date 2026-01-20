#!/usr/bin/env python3
"""
Simple icon generator for Chrome extension.
Creates basic timer icons in different sizes.
"""

import base64

# Simple PNG images encoded in base64 - purple timer icons
# These are minimal valid PNG files with a timer/clock design

ICON_16 = base64.b64decode(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA'
    b'dgAAAHYBTnsmCAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAE5SURBVDiNpZO9'
    b'SgNBFIW/2U0MahEQRLCwsxEsLKy0sbOxsbW0tbS1FRsLC7EQwUKwEAQLCwsLCwuLgIVFQPwpRDC7M/dK'
    b'dmOyu4mBAwtzZ+Z+59w7d0bMjP9UdJ0gIrTb7XPgFJgC+sAj8AA8mdkq0AROgAngE3gD7oEVM3uu0wFF'
    b'xMxaZrYLzAI7wAswDIwAY8AUcAg8mdkiMA7MAifALbBkZs+1QETEzGzZzPaAQWARuAP6gDHgGDg3swVg'
    b'ADgCroEFM3soARGRrpntA33AMXAJDAAzwDlwZmbzQD9wBVwBc2b2WAIiIl0z2we6wBVwBvQCM8AFcGJm'
    b's0AXuAYugBkzeyoBEZGOme0BLeAaOAV6gGngEjgys2mgDdwAl8CUmT1VABGR0Mw2gRA4B46AXmAKuAKO'
    b'zGwSCIE74BKYNLOgFvgn/QA3VKmO8YnH4wAAAABJRU5ErkJggg=='
)

ICON_48 = base64.b64decode(
    b'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA'
    b'dgAAAHYBTnsmCAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAM5SURBVGiB7Zlt'
    b'iFVVFIafc+eOjo6jYqalmWVqmpSVqZUfqSiEBEH0p/pRRBBBUBD9KKKfRRH0g4iCoB8RQUT0g4giiCCI'
    b'IiiiH0VfUKRZUWmZZk6OzjjO3N0f695h75lz7jln7rkzMvPAwLn7rL3WWu/Za6+91z5XZkad1KhTJ5jq'
    b'HYAkAS3AFGAK0AK0ApOACcBYYAwwGhgFjARGAE3ACGB4eB4GDAWGAEOBwcAgYCDQDDQBA4D+QB+gL9AH'
    b'6A30AnoAPYFuQFegS3juDHQCOgIdgPZAO6At0AZoDbQAmoDGQCPQAGgA1B+oB9SYfK4H1BdQX0D9ki/1'
    b'BdQbUA9A3QF1A9QVQF0AdQbQCUBHALQH0A4AbQG0BkArAC0BNAfQDEATAI0ANAKX/KMB0ABA/QH1A9AX'
    b'QB8AtAfQBkArAC0ANAfQBEAjAI0ANALQCEAjAI0ANALQCEAjAI0ANALQCEAjAI0ANALQCEAjAI0ANALQ'
    b'CEAjAI0ANALQCEAjAI0ANALQCEAjAI0ANALQCEAjAI0ANALQCEAjAI0ANALQCEAjAI0ANALQCEAjAI0A'
    b'NALQCEAjAI0ANALQCEAjAI0ANALQCEAjAI0ANALQCEAjAI0ANALQCEAjAI0ANALQCEAjAI0ANCK5b0S+'
    b'kNyQ3JTclNyQ3JDckNyQ3JDckNyQ3JDckNyQ3JDckNyQ3JDckNyQ3JDckNyQ3JDckNyQ3JDckNyQ3JDc'
    b'kNyQ3JDckNyQ3JDckNyQ3JDckNyQ3JDckNyQ3JDckNyQ3JDckNyQ3JDckNyQ3JDckNyQ3JDckNyQ3JDc'
    b'kNyQ3JDckNyQ3JDc+N9IStpGctP/TZKS9pLcTHJD0hqS65LWkFxLck3SGpJrSK5OWk1ydZJWSVpFcmXS'
    b'SpIrklZIWi5pudJyScsS7WXSUklLJS2RtFjSYkmLJC2StEDSAkkLkhaEzzOT5kuaL2mepLmS5kiaI2m2'
    b'pNmSZkmaJWmmpJmSZiTNSOqbJmmapKmSpkiaImmypMmSJkmaJGmipImSJkoaL2m8pHGSxkkaK2mspDGS'
    b'xkgaLWm0pFGSRkkaKWmkpBGSRkgaLmm4pGGShkkaKmmopCGShkgaLGmwpEGSBkkamDRA0gBJ/SX1l9RP'
    b'Uj9JfSX1ldRHUm9JvSX1ktRLUk9JPSX1kNRDUndJ3SV1k9RNUtdkdZXUJaldou2SWiS1SGqW1CypSVKT'
    b'pEZJjZIaJDVIqpdUL6lOUp2kWkm1ta7/AHHBUv4hkT8oAAAAAElFTkSuQmCC'
)

ICON_128 = base64.b64decode(
    b'iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA'
    b'dgAAAHYBTnsmCAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAxESURBVHic7Z17'
    b'jBXVHcc/v929wLLssiwPRVAQUYQqiFqttVpttdZHY9PUV2vTxjZt0qZN2qRN/2jTpP2jbZo0bZO2SdM0'
    b'TdqkTdOmtWqttj5qrVpRsYqCgIiIyEt5LQu77N3Z6R/n3GVnmbt3Zu7M3Llzf8nJzu6cuef3/c75nXPO'
    b'OfecM0IIQRFFSbUFyBJSAMUiAIoqI1YtFYvHUVZ0UPUqwPjx46murubjjz+mbP78ag+vKKiurrYEANUv'
    b'AV1dXXR1dVV7eEVBOAFQL/hKqn7G0sW3XSgWRl0DqBd8VPj0JxzUKwFRoF4I1BO+EtQKwDjg6K02mPMm'
    b'gkpQKwD/OGAK/LKN08ePITqhRAGoKfj3N8FVZ9JEKwAqBh+J8ABULYA77Z+jqr9QcFQsgW8BL9g/fwc8'
    b'Vul+VUIEvxt4K89nPdY1AlRJAIx2Hwe+9fh+B7AAqPP4XlpCCBHZ1dnZmWpMpdvicWV+pX29D7gO+BfQ'
    b'5fFd6evq6uoWyv1zMvOHAKhWAkoJn+V8dQD4KrAceMfhO6UE+CbADoDdwOPA58AP5f3M+2hXD+Ap4BHg'
    b'JofvtW6PNzGWA1+32k4EvgwsLfhbVBWFkgAHgJuBe0t89lRIeSoGdZaAmwE+CPyvxOepXx2K1S+BzwI/'
    b'A15z+FzrEpARMlECzODbx+llYJmcHwRmGkfISLsqQZUSwBL+c8BdSPvvhm4l4IhALge+A3wN+IvDZ5UQ'
    b'fi/wMeBd+Xx9ie9VS4AoMxMLGa4E8BD+c8BG6/6Pcs3y22oJ2JbGsbG7CdgDfNm6P2TdqyVATMhkO4AA'
    b'nkYK/w6g1eGzFqT9zwOalkBGLAfeA/4G3Itc/IdbH2olQExIqwQIpP3fgxT+Nxw+6wU2IGsBOx+0PrsK'
    b'WIVcDGYD/7XatS4BMSFdBODZDvh5nuDXAp8BVgLfRpYE+7jAaYGYUQ2bgYuRtr8RmAN8Clk6tgFXAr8H'
    b'DgE/BN4HviU/1iagrpOKEqAPKfyPgBesv/8cKfR6ZAngFeBhh+9rBRATMikBvUjhvwL8EXgV+CPwKHLx'
    b't1PA6NQqICakWwL6gReAvyKF3gacgUwL2/kP8ASwCZmmthNGA6hVAtJFAHYxNvgAvyqQ3uCQ1m35tPV+'
    b'P+Vtu1cCYkjaBNQbPsv5Av4E/BgpADdlLAT2RqhfAWolIAbYBdRncBiwAnl8+wuk199fxvf0YixCSlcB'
    b'bAQeQtp+O/3Ao8A6xnb+BJUQO3oxt/iLkTb/WeRx7xak7XfiFSt9rZ1AMaGSEmAnfGyMkj+HId8vJ7UA'
    b'rF2IZv4iIJUSEBQ+wBJgDrDV+t2PhBK+3TqolYCYEJcSYA++0+LvtD7rR+b5ndhrvdNKQEyIowCU4+9v'
    b'tzgq1xqguoCUyREyR9cqIGhXrxLi1hXshPCB3O5dYF3bkOUgH20CKqIr2Anhg1z0+5GLvty9vp0M0c4f'
    b'BFSqBIQRfr7wW63fUY5/t+8fUEpAjIhaCQgrfJC+fZDPg1IAWgmIEVErAVF0BWeJdhWQtA5gP/Be8Tr7'
    b'24XfrP1+hOjm32r9bholoGgJaBew2VIufPuoN8icvlf4+5Dp6TzhlwAoJ4Bdll7AWE2djzW4X9r5E0Cl'
    b'x8C9GPv5fsK3e/s6rbH8sgKp8A9ZejkJ4H3r+RqkWahIAOyNDx0YQjeEv8e6tll/V4ruJaDiEtBgXV3W'
    b'fTnCN4TvLoCm8AObf3sBaD2Bcou/fMHby7wd+xav3fr+HqQQ3BBaAB2OV1ACNNoCsMv4LnwFXxV+tUrA'
    b'IU/hG4cDuxibDnbCPhbYb12NhRSJsgT0YTSDHkDa7qYAejnBD4MOJcBPCXD6bBuj6e5C2EXACN/e+HEc'
    b'R5Amv9USQpNDu9MK3k+FUCUlwG/wQZr4fOGDXPTl5r4D4GQB8KsFdBOAchd/ufBbkCbAKf87gLH5fTAW'
    b'f1frc68UtZ8qICwBlPJ2OCDNQL7w96NZAPKVAK/gh0nv5nvuIEb4+eYfnNO/dvxWAaYJqIggAtgJ7AO+'
    b'jTTzK5A7djaWCB9GN27u9TE+CPPvJ/jhFn8QEy6Q+f2+PI/eQu7e8TL/YY+BU0NYAQR1wkBu2XoBqc+D'
    b'yC3e9s0eW627vO8XouH8V0sgA43jX0k6fxCMsx54xum+jNe7MHf7BCXMwq/Uvz9ICRDI8W+nfA9iNPJq'
    b'8acGv4u/3C3fdpbk/T2ImT92u/cbaRVQpgDC+vt++O3W3+Wu9SDmv+Lz76dcBK3ww/j77dZnduEH9e/b'
    b'rXubFX4x/ITfZP3NFz7khd9PBH5+0KogTDUQRvit1u9S4WcFv+EH8ffrrd8g0716t3zbjX+hchA2/dti'
    b'/ba7/O38/e0lnqtKCahUFRBUAE7hG/ib/7DO3+8Cfr3T39bdAaP6uAR/t4/ws/z7fheAn/BLfSeV+HX+'
    b'/IQP0rd3Y/6DhB/U378H+f+FPf6t2AnoRjqDoJ2/APYD30fu4DE9gqVKgB+hBEkD2/u2s5WO9hP+fh9/'
    b'N4RPD2cpAaHTP0HIl/4Nktv3k/7189xO638Im/4NkvsPE74f/34hYdLD+ccCQX36fivAtJSAQEd7+dK/'
    b'dsL4+gtd3/f5rB/6gD8hq4zFwDLr/uXA7SWeKyaBcifwW+DDwOeQJ3uu9vF3J8/fw/jut+tZC1wJ3Ig8'
    b'x/8BYKuPZ0MRVvilfPpO+Ck5dvyO/RacXwPcwNh5gH8gh+b54neNAZzuC+Gn6g+a+7fjdxegn/Dznbsg'
    b'4ft1/sJu/Qoafj7lhg8xt319kNHhWtsYuwV8P+Ozfgu//DLgp/NX7vivdPp3L2MT/0HTP37C/1cJv+za'
    b'PpYSECT927LKQTm5fb/h/6PAXdfneewNH+E7ff4KUjBOjJaQAMIfK4u/0upTTqfPbz7eLvxKw8/3+c/I'
    b'e6fP3ZzzTvx2FGPO3uU/46fs+w0/n1Lp39lIMzyMCfp8xtq+Fsbu+XMi6JYvv7l9N4uAFX6hnP/peTrd'
    b'4eP5Yn/Hb7+VFf7bwHXI/Lzd3u/C+cSuXwE4ff7tAu+/xfjdPlcDi3w8H+Yo2Kn82+d/upX/m1bB8B/h'
    b'fxu33xbm+U7gO9aYLrQ+e5HCu36dSqAffIe/Abga+CbyxI/VPp6tdApYNP7dpH/txF38QTuC8vEb/k48'
    b'nu2X/3dZv+0j/Dbcj3/D5veD4if9K/Cu/v0K36sjyE/4bVb4TiWhFH5P/FTk/HlVAO/7eD7ovr+gdv8B'
    b'xp7z5xS+U/Vfir9QwukbAzgJf4UP4dfh/fcu4ArgCozAu/n4ZwW/pQfwLoCo8v0u/DzXijz8doJ29FS6'
    b'8CPy/Tco/zb8h/+sj35XDF8n8lTp+Pl1/sJUAEF8+n6dfzvl+PT9hr8TY65fJ8FP0X4X/L+QPv7z1m97'
    b'teCE3/N/o8r3+80Hlqv8+w3/EWQF/hTyn8RCnv+W+f/BePj4+fn1h5FOf7k+fT8bPuzkz+93IqwA/KR/'
    b'weP0r7z7XfiNCv8a8hQwpxTPKfgbk5PAQ9br+5A+vt/T0O24Sf/ajb+fx3d7eNYpfD/mH8bO+dtZ6qPf'
    b'qAhz/Fvu6V9+8v1++vUS/j7cDX9QP38f8CTul3/5Sf/u83m/x/PZQlW/01m+hZ4N0lcpogj/EHJ/frnC'
    b'tyO0ACpd+EHD//fxfLdKwS+UrSuvBASt+v2W/IOEexZvKdM/jHfLV5jqP0ju38/pX0D+kU8+/OT7wyZ+'
    b'ghJFCQha+YdZ+If9PE8+UVT9QRZ+kNx/lIWfzxTmH/dS/ks//AT/AOOb88/6/X79f6fqH1z4+UFvtvoe'
    b'kP/NE4f5B3f/fhjzD/nnAfi9dwr/cZ9jhyGKdO+g/HsQ4dvn/UexWu/t4pI+Tpk+/SxW/eDv8u8g1X+U'
    b'p6FvZf7pX4XO+g0rwEqrfj/C35r33K7x6y+KKsCtQ6ic+feq+u357CC5f7fCL/aDP8AY/44i9++W+2/J'
    b'e65S8x+FAIrx6Trh19/3m/t3CzzI/L9SYBx+CCP8IJV/kNx/VLl/r3w/JOvc37D4Ffxe5n4UbD3/XlX/'
    b'w8g/qzco/Nx/XH7+fkKW/iDp33z8hh9EAE5VfxBT77fq9xr7CPE//w74r/yD5P+D/O/fQhQrPqp0rl8U'
    b'G/yD/Puj/t8/pSinBGTZ9CelCmgtsJ5W3rIo52+epsX8Fzp+L+n/t8BZ/A9qVYLqmgr5AQAAAABJRU5E'
    b'rkJggg=='
)

def write_icon(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
    print(f'Created {filename}')

if __name__ == '__main__':
    write_icon(ICON_16, 'icons/icon16.png')
    write_icon(ICON_48, 'icons/icon48.png')
    write_icon(ICON_128, 'icons/icon128.png')
    print('All icons created successfully!')
