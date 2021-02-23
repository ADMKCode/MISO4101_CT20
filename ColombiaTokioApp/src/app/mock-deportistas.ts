import { Deportista } from './deportista'

export const DEPORTISTAS: Deportista[] =
[
  {
    id: 1,
    user: 'Óscar Figueroa',
    fecha_nacimiento: '27/04/1983',
    peso: 62,
    estatura: 165,
    entrenador: 'Gregorio Diaz',
    imagen: 'https://thebogotapost.com/wp-content/uploads/2016/08/RIOEC881RBXRY_768x432.jpg',
    lugar_nacimiento:{departamento: 'Antioquia', ciudad: 'Zaragoza'}
  },
  {
    id: 2,
    user: 'Rogelio Rios',
    fecha_nacimiento: '27/04/1983',
    peso: 60,
    estatura: 170,
    entrenador: 'Raul Roltz',
    imagen: 'https://www.thenationalnews.com/image/policy:1.704781:1518673464/Pyeongchang-2018-Winter-Olympics.JPG?f=16x9&w=1200&$p$f$w=22355b3',
    lugar_nacimiento:{departamento: 'Santander', ciudad: 'Bucaramanga'}
  }
]
