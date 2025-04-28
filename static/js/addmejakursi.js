


// Meja Lantai 1
    const L1table = L.layerGroup();

// Koordinat dan data meja
    const tables1 = [
    //PST
        //pelayanan
        { coords: [11, 9], imageUrl: `${staticUrl}mejabawah.png`, width: 14, height: 6 },
        //pengaduan
        { coords: [11, 33], imageUrl: `${staticUrl}mejabawah.png`, width: 14, height: 6 },
        
   //IPDS
        //ipds1
        { coords: [91.5, 46], imageUrl: `${staticUrl}mejakanan.png`, width: 6, height: 12 },
        //ipds2
        { coords: [106.5, 46], imageUrl: `${staticUrl}mejakanan.png`, width: 6, height: 12 },
        //ipds3
        { coords: [121.5, 46], imageUrl: `${staticUrl}mejakanan.png`, width: 6, height: 12 },
        //ipds4
        { coords: [140, 63], imageUrl: `${staticUrl}mejabawah.png`, width: 12, height: 6 },
        //ipds5
        { coords: [140, 76], imageUrl: `${staticUrl}mejabawah.png`, width: 12, height: 6 },

        //server
        { coords: [146, 90], imageUrl: `${staticUrl}server.png`, width: 11, height: 6 },

    ];

    // Menambahkan gambar overlay ke peta
    tables1.forEach(({ coords, imageUrl, width, height }) => {
        const bounds = [
            [coords[0] - height / 2, coords[1] - width / 2], // Koordinat sudut kiri atas
            [coords[0] + height / 2, coords[1] + width / 2], // Koordinat sudut kanan bawah
        ];

        const overlay = L.imageOverlay(imageUrl, bounds, { pane: 'tablePane' });
        overlay.addTo(L1table);
    });

    // Kursi Lantai 1
    const L1chair = L.layerGroup();

    // Koordinat dan data meja
    const chairs1 = [
        //pelayanan
        { coords: [4.5, 9], imageUrl: `${staticUrl}kursiatas.png`, width: 5, height: 5 },
        //pengaduan
        { coords: [4.5, 33], imageUrl: `${staticUrl}kursiatas.png`, width: 5, height: 5 },

        //ipds1
        { coords: [91, 52], imageUrl: `${staticUrl}kursikiri.png`, width: 5, height: 5 },
        //ipds2
        { coords: [106, 52], imageUrl: `${staticUrl}kursikiri.png`, width: 5, height: 5 },
        //ipds3
        { coords: [121, 52], imageUrl: `${staticUrl}kursikiri.png`, width: 5, height: 5 },
        //ipds4
        { coords: [146, 63], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },
        //ipds5
        { coords: [146, 76], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },
        //server
        { coords: [140, 90], imageUrl: `${staticUrl}kursiatas.png`, width: 5, height: 5 },
        
    ];


    // Menambahkan gambar overlay ke peta
    chairs1.forEach(({ coords, imageUrl, width, height }) => {
        const bounds = [
            [coords[0] - height / 2, coords[1] - width / 2], // Koordinat sudut kiri atas
            [coords[0] + height / 2, coords[1] + width / 2], // Koordinat sudut kanan bawah
        ];

        const overlay = L.imageOverlay(imageUrl, bounds, { pane: 'chairPane' });
        overlay.addTo(L1chair);
    });



// Meja Lantai 2
    const L2table = L.layerGroup();

// Koordinat dan data meja
    const tables2 = [
    //Tata Usaha
        //tu1
        { coords: [129, 162], imageUrl: `${staticUrl}mejapanjangatas.png`, width: 18, height: 6 },

    //Tata Usaha Cubicle
        //tua
        { coords: [129, 183], imageUrl: `${staticUrl}mejakosongh.png`, width: 9, height: 6 },
        //tub
        { coords: [129, 192], imageUrl: `${staticUrl}mejakosongh.png`, width: 9, height: 6 },
        //tu2 cubicle
        { coords: [132, 204], imageUrl: `${staticUrl}cubicle4.png`, width: 12, height: 12 },
        //tu3 cubicle
        { coords: [132, 216], imageUrl: `${staticUrl}cubicle3.png`, width: 12, height: 12 },
        //tu4 cubicle
        { coords: [120, 216], imageUrl: `${staticUrl}cubicle2.png`, width: 12, height: 12 },
        //tu5 cubicle
        { coords: [120, 204], imageUrl: `${staticUrl}cubicle1.png`, width: 12, height: 12 },

        //tuc
        { coords: [123, 192], imageUrl: `${staticUrl}mejakecilbawah.png`, width: 9, height: 6 },
        //tud
        { coords: [123, 183], imageUrl: `${staticUrl}mejakosongh.png`, width: 9, height: 6 },

    //Tata Usaha setengah cubicle
        //tu6
        { coords: [98, 168], imageUrl: `${staticUrl}cubicle1.png`, width: 12, height: 12 },
        //tu7
        { coords: [98, 180], imageUrl: `${staticUrl}cubicle2.png`, width: 12, height: 12 },

    //Teknis Meja Katim
        //teknis1
        { coords: [7, 155], imageUrl: `${staticUrl}mejakiri.png`, width: 6, height: 12 },
        //teknis3
        { coords: [4, 180], imageUrl: `${staticUrl}mejaatas.png`, width: 12, height: 6 },
        //teknis4
        { coords: [4, 195], imageUrl: `${staticUrl}mejaatas.png`, width: 12, height: 6 },
        //teknis5
        { coords: [4, 213], imageUrl: `${staticUrl}mejaatas.png`, width: 12, height: 6 },
        //teknis6
        { coords: [4, 228], imageUrl: `${staticUrl}mejaatas.png`, width: 12, height: 6 },
        //teknis8
        { coords: [7, 253], imageUrl: `${staticUrl}mejakanan.png`, width: 6, height: 12 },


    //Cubicle Teknis Group 1
        //teknis9
        { coords: [27, 152], imageUrl: `${staticUrl}cubicle1.png`, width: 12, height: 12 },
        //teknis10
        { coords: [27, 164], imageUrl: `${staticUrl}cubicle2.png`, width: 12, height: 12 },
        //teknis11
        { coords: [39, 164], imageUrl: `${staticUrl}cubicle3.png`, width: 12, height: 12 },
        //teknis12
        { coords: [39, 152], imageUrl: `${staticUrl}cubicle4.png`, width: 12, height: 12 },

    //Cubicle Teknis Group 2
        //teknis13
        { coords: [27, 180], imageUrl: `${staticUrl}cubicle1.png`, width: 12, height: 12 },
        //teknis14
        { coords: [27, 192], imageUrl: `${staticUrl}cubicle2.png`, width: 12, height: 12 },
        //teknis15
        { coords: [39, 192], imageUrl: `${staticUrl}cubicle3.png`, width: 12, height: 12 },
        //teknis16
        { coords: [39, 180], imageUrl: `${staticUrl}cubicle4.png`, width: 12, height: 12 },  

    //Cubicle Teknis Group 3
        //teknis17
        { coords: [27, 216], imageUrl: `${staticUrl}cubicle1.png`, width: 12, height: 12 },
        //teknis18
        { coords: [27, 228], imageUrl: `${staticUrl}cubicle2.png`, width: 12, height: 12 },
        //teknis19
        { coords: [39, 228], imageUrl: `${staticUrl}cubicle3.png`, width: 12, height: 12 },
        //teknis20
        { coords: [39, 216], imageUrl: `${staticUrl}cubicle4.png`, width: 12, height: 12 },  
    
    //Cubicle Teknis Group 4
        //teknis21
        { coords: [27, 244], imageUrl: `${staticUrl}cubicle1.png`, width: 12, height: 12 },
        //teknis22
        { coords: [27, 256], imageUrl: `${staticUrl}cubicle2.png`, width: 12, height: 12 },
        //teknis23
        { coords: [39, 256], imageUrl: `${staticUrl}cubicle3.png`, width: 12, height: 12 },
        //teknis24
        { coords: [39, 244], imageUrl: `${staticUrl}cubicle4.png`, width: 12, height: 12 },    
    ];

    // Menambahkan gambar overlay ke peta
    tables2.forEach(({ coords, imageUrl, width, height }) => {
        const bounds = [
            [coords[0] - height / 2, coords[1] - width / 2], // Koordinat sudut kiri atas
            [coords[0] + height / 2, coords[1] + width / 2], // Koordinat sudut kanan bawah
        ];

        const overlay = L.imageOverlay(imageUrl, bounds, { pane: 'tablePane' });
        overlay.addTo(L1table);
    });

// Kursi Lantai 2
    const L2chair = L.layerGroup();

// Koordinat dan data meja
    const chairs2 = [
    //TATA USAHA
        //tu1
        { coords: [135, 162], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },

    //meja pkl
        //tua
        { coords: [135, 183], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },
        //tub
        { coords: [135, 192], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },

    //Cubicle Tata Usaha
        //tu2 cubicle
        { coords: [134, 201], imageUrl: `${staticUrl}kursikanan.png`, width: 5, height: 5 },
        //tu3 cubicle
        { coords: [134, 219], imageUrl: `${staticUrl}kursikiri.png`, width: 5, height: 5 },
        //tu4 cubicle
        { coords: [118, 219], imageUrl: `${staticUrl}kursikiri.png`, width: 5, height: 5 },
        //tu5 cubicle
        { coords: [118, 201], imageUrl: `${staticUrl}kursikanan.png`, width: 5, height: 5 },

    //meja pkl
        //tuc
        { coords: [117, 183], imageUrl: `${staticUrl}kursiatas.png`, width: 5, height: 5 },
        //tud
        { coords: [117, 192], imageUrl: `${staticUrl}kursiatas.png`, width: 5, height: 5 },

    //meja bendahara ppk
        //tu6
        { coords: [96, 183], imageUrl: `${staticUrl}kursikiri.png`, width: 5, height: 5 },
        //tu7
        { coords: [96, 165], imageUrl: `${staticUrl}kursikanan.png`, width: 5, height: 5 },

    //TEKNIS
        //Horizontal selatan
        { coords: [7, 149], imageUrl: `${staticUrl}kursikanan.png`, width: 5, height: 5 },
        { coords: [10, 180], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },
        { coords: [10, 195], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },
        { coords: [10, 213], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },
        { coords: [10, 228], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },
        { coords: [7, 259], imageUrl: `${staticUrl}kursikiri.png`, width: 5, height: 5 },

    //Cubicle Teknis
        //Cubicle Teknis Grup 1
        { coords: [24, 149], imageUrl: `${staticUrl}kursiatas.png`, width: 5, height: 5 },
        { coords: [24, 166], imageUrl: `${staticUrl}kursiatas.png`, width: 5, height: 5 },
        { coords: [42, 166], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },
        { coords: [42, 149], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },

        //Cubicle Teknis Grup 2
        { coords: [24, 178], imageUrl: `${staticUrl}kursiatas.png`, width: 5, height: 5 },
        { coords: [24, 194], imageUrl: `${staticUrl}kursiatas.png`, width: 5, height: 5 },
        { coords: [42, 194], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },
        { coords: [42, 178], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },

        //Cubicle Teknis Grup 3
        { coords: [24, 214], imageUrl: `${staticUrl}kursiatas.png`, width: 5, height: 5 },
        { coords: [24, 230], imageUrl: `${staticUrl}kursiatas.png`, width: 5, height: 5 },
        { coords: [42, 230], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },
        { coords: [42, 214], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },

        //Cubicle Teknis Grup 4
        { coords: [24, 242], imageUrl: `${staticUrl}kursiatas.png`, width: 5, height: 5 },
        { coords: [24, 258], imageUrl: `${staticUrl}kursiatas.png`, width: 5, height: 5 },
        { coords: [42, 258], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },
        { coords: [42, 242], imageUrl: `${staticUrl}kursibawah.png`, width: 5, height: 5 },
        
    ];


    // Menambahkan gambar overlay ke peta
    chairs2.forEach(({ coords, imageUrl, width, height }) => {
        const bounds = [
            [coords[0] - height / 2, coords[1] - width / 2], // Koordinat sudut kiri atas
            [coords[0] + height / 2, coords[1] + width / 2], // Koordinat sudut kanan bawah
        ];

        const overlay = L.imageOverlay(imageUrl, bounds, { pane: 'chairPane' });
        overlay.addTo(L1chair);
    });
