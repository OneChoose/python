
import execjs


def excuteScript():

    jsFunc1 = '''
        function ep(TG) {
                var qo, mo = "", no = "", oo = [0xaf, 0xb4, 0x62, 0xf7, 0x9f, 0x56, 0xf5, 0x8d, 0x30, 0xd8, 0x30, 0x11, 0xa8, 0x4a, 0xeb, 0xbe, 0x5c, 0xf7, 0x8f, 0x7f, 0x9f, 0x79, 0x0b, 0xb8, 0x4f, 0x39, 0xd0, 0x6f, 0x07, 0x9c, 0x91, 0x38, 0xcb, 0x6e, 0x04, 0x80, 0x18, 0x08, 0xec, 0xd7, 0xf4, 0xd8, 0xc2, 0xab, 0x8f, 0x03, 0x9d, 0x88, 0x70, 0x04, 0x64, 0xf9, 0x91, 0x25, 0xbe, 0x37, 0x24, 0xb9, 0xa1, 0x38, 0x24, 0x0f, 0xfb, 0x93, 0x7c, 0x56, 0x3d, 0x22, 0x02, 0xe5, 0x57, 0xf0, 0xd8, 0xbd, 0x9d, 0x6b, 0x54, 0x3e, 0xd8, 0xc0, 0x42, 0x22, 0xb5, 0x50, 0x3a, 0xa4, 0x38, 0x18, 0xfe, 0x95, 0x65, 0x49, 0xe1, 0xca, 0x60, 0x3c, 0x28, 0x0d, 0xa4, 0x8c, 0x70, 0x04, 0xee, 0xce, 0xb2, 0x0a, 0xf1, 0xda, 0xc2, 0xa8, 0x67, 0x4c, 0x31, 0x15, 0xfe, 0xe1, 0xc9, 0xb7, 0x8c, 0x24, 0xda, 0x85, 0x2a, 0xc5, 0x6c, 0x0d, 0xa6, 0x4c, 0x3c, 0xc4, 0xad, 0x4a, 0xf1, 0xd2, 0xa5, 0x0e, 0xf4, 0xd7, 0xb7, 0x30, 0x33, 0xcc, 0x62, 0x42, 0x26, 0xe5, 0xd2, 0xa5, 0x89, 0x6e, 0xe6, 0xd3, 0xb9, 0xa1, 0x90, 0x1a, 0x02, 0xe9, 0xbe, 0x38, 0x8e, 0x0e, 0x96, 0x84, 0x57, 0xe5, 0x7e, 0x20, 0xbf, 0x53, 0x19, 0xb6, 0x57, 0x47, 0x2a, 0xa4, 0x8d, 0x78, 0x14, 0xb8, 0x0b, 0xed, 0x83, 0x26, 0x14, 0xfb, 0xd0, 0x73, 0x07, 0xaf, 0x2f, 0xcb, 0xbb, 0x9d, 0x77, 0x38, 0x26, 0xfa, 0xa4, 0x40, 0xa4, 0x45, 0xdd, 0x7f, 0x29, 0xba, 0x9b, 0x34, 0xd5, 0x6b, 0x99, 0x41, 0xe2, 0x7a, 0x1b, 0x6a, 0x11, 0xf3, 0x94, 0x36, 0x34, 0xc9, 0x5d, 0x06, 0xa1, 0x1c, 0xbd, 0x60, 0x50, 0xe8, 0x3b, 0xde, 0x74, 0x1c, 0xbb, 0x31, 0xca, 0x6b, 0x14, 0xf6, 0x0a, 0x91, 0x18, 0xdb, 0x3b];
                qo = "qo=243; do{oo[qo]=(-oo[qo])&0xff; oo[qo]=(((oo[qo]>>1)|((oo[qo]<<7)&0xff))-32)&0xff;} while(--qo>=2);";
                eval(qo);
                qo = 242;
                do {
                    oo[qo] = (oo[qo] - oo[qo - 1]) & 0xff;
                } while (--qo >= 3);qo = 1;
                for (; ; ) {
                    if (qo > 242)
                        break;
                    oo[qo] = ((((((oo[qo] + 118) & 0xff) + 3) & 0xff) << 1) & 0xff) | (((((oo[qo] + 118) & 0xff) + 3) & 0xff) >> 7);
                    qo++;
                }
                po = "";
                for (qo = 1; qo < oo.length - 1; qo++)
                    if (qo % 5)
                        po += String.fromCharCode(oo[qo] ^ TG);
                return po;
            }
    
    '''
    jsContext = execjs.compile(jsFunc1)
    antipas = jsContext.call('ep', 62)
    return antipas

print(excuteScript())