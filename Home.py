from random import randrange, uniform
from IPython.display import clear_output

#dia 1

Hangul = ['안녕하세요', '네', '아니요', '미안합니다', '감사합니다', '사랑', '가다', '오다', '먹다', '마시다', '잠 ', '물', '나', '너', '우리', '그 ', '이', '그리고', '누구', '무엇 ', '이해', '도움', '시간', '돈', '문제', '친구', '가족', '학교', '음식', '주다', '받다', '보다', '듣다', '말하다', '공부하다', '일하다', '좋다', '싫다', '크다', '작다', '높다 ', '낮다', '색', '날씨', '가다', '오다', '좋아하다', '싫어하다', '생일', '시간']
Portugues = ['Olá', 'Sim', 'Não', 'Desculpe', 'Obrigado(a)', 'Amor', 'Ir', 'Vir', 'Comer', 'Beber', 'Sono', 'Água', 'Eu', 'Você', 'Nós', 'Aquilo', 'Este', 'E', 'Quem', 'O que', 'Entendimento', 'Ajuda', 'Tempo', 'Dinheiro', 'Problema', 'Amigo', 'Família', 'Escola', 'Comida', 'Dar', 'Receber', 'Ver', 'Ouvir', 'Falar', 'Estudar', 'Trabalhar', 'Gostar', 'Não gostar', 'Grande', 'Pequeno', 'Alto', 'Baixo', 'Cor', 'Tempo (clima)', 'Ir', 'Vir', 'Amar, gostar', 'Odiar, não gostar', 'Aniversário', 'Tempo, hora']
Romanizado = ['annyeonghaseyo', 'ne', 'aniyo', 'mianhamnida', 'gamsahamnida', 'sarang', 'gada', 'oda', 'meokda', 'masida', 'jam', 'mul', 'na', 'neo', 'uri', 'geu', 'i', 'geurigo', 'nugu', 'mueot', 'ihae', 'doum', 'sigan', 'don', 'munje', 'chingu', 'gajok', 'hakgyo', 'eumsik', 'juda', 'batda', 'boda', 'deutda', 'malhada', 'gongbuhada', 'ilhada', 'jota', 'silta', 'keuda', 'jakda', 'nopda', 'natda', 'saek', 'nalssi', 'gada', 'oda', 'joahada', 'silheohada', 'saengil', 'sigam']

#dia 2

Hangul2 = [
    "어디", "지금", "학생", "선생님", "부모님", "남자", "여자", "아이", "남편", "아내",
    "형", "누나", "동생", "친척", "숙제", "여행", "휴가", "영화", "음악", "책",
    "가방", "신발", "옷", "노래", "차", "비행기", "기차", "버스", "자전거", "스마트폰",
    "컴퓨터", "텔레비전", "라디오", "식사", "아침", "점심", "저녁", "과일", "채소", "고기",
    "빵", "우유", "커피", "차", "물", "사진", "카메라", "쇼핑", "가격", "돈",
    "할인", "현금", "신용카드", "병원", "약국", "의사", "간호사", "아프다", "건강", "병",
    "약", "행복", "슬픔", "화", "놀다", "즐기다", "웃다", "울다", "춤", "노래하다",
    "읽다", "쓰다", "그림", "사람", "꽃", "나무", "하늘", "구름", "해", "달",
    "별", "바다", "강", "산", "공원", "국제공항", "호텔", "박물관", "영어", "한국어",
    "번역", "쉽다", "어렵다", "많다", "적다", "빠르다", "느리다", "예쁘다", "멋있다", "좋다",
    "나쁘다", "덥다", "추울다"
]

Portugues2 = [
    "Onde", "Agora", "Estudante", "Professor(a)", "Pais", "Homem", "Mulher", "Criança", "Marido", "Esposa",
    "Irmão mais velho", "Irmã mais velha", "Irmão/Irmã mais novo(a)", "Parente", "Tarefa de casa", "Viagem", "Férias", "Filme", "Música", "Livro",
    "Bolsa/mochila", "Sapato", "Roupa", "Canção", "Chá/carro", "Avião", "Trem", "Ônibus", "Bicicleta", "Smartphone",
    "Computador", "Televisão", "Rádio", "Refeição", "Manhã", "Almoço", "Jantar", "Fruta", "Vegetais", "Carne",
    "Pão", "Leite", "Café", "Chá", "Água", "Foto", "Câmera", "Compras", "Preço", "Dinheiro",
    "Desconto", "Dinheiro em espécie", "Cartão de crédito", "Hospital", "Farmácia", "Médico", "Enfermeira", "Estar doente", "Saúde", "Doença",
    "Remédio", "Felicidade", "Tristeza", "Raiva", "Brincar", "Divertir-se", "Rir", "Chorar", "Dança", "Cantar",
    "Ler", "Escrever", "Desenho", "Pessoa", "Flor", "Árvore", "Céu", "Nuvem", "Sol", "Lua",
    "Estrela", "Mar", "Rio", "Montanha", "Parque", "Aeroporto internacional", "Hotel", "Museu", "Inglês", "Coreano (língua)",
    "Tradução", "Fácil", "Difícil", "Muito", "Pouco", "Rápido", "Lento", "Bonito(a)", "Elegante", "Bom",
    "Ruim", "Quente", "Frio"
]

Romanizado2 = [
    "eodi", "jigeum", "haksaeng", "seonsaengnim", "bumonim", "namja", "yeoja", "ai", "nampyeon", "ane",
    "hyeong", "nuna", "dongsaeng", "chinjaek", "sukje", "yeohaeng", "hyuga", "yeonghwa", "eumak", "chaek",
    "gabang", "sinbal", "ot", "nolae", "cha", "bihaenggi", "gicha", "beoseu", "jajeongeo", "seumaeteupon",
    "keompyuteo", "tellebijeon", "radio", "siksa", "achim", "jomsim", "jeonyeok", "gwail", "chaeso", "gogi",
    "ppang", "uyu", "keopi", "cha", "mul", "sajin", "kamera", "syoping", "gageuk", "don",
    "halin", "hyeongeum", "sinyongkadeu", "byeongwon", "yagguk", "uisa", "ganhosa", "apeuda", "geongang", "byeong",
    "yak", "haengbok", "seulpeum", "hwa", "nolda", "jeulgida", "utda", "ulda", "chum", "noraehada",
    "ikda", "sseuda", "geurim", "saram", "kkot", "namu", "haneul", "gureum", "hae", "dal",
    "byeol", "bada", "gang", "san", "gongwon", "gukjegonghang", "hotel", "bakmulgwan", "yeongeo", "hangugeo",
    "byeonryeok", "swibda", "eoryeobda", "manhda", "jeokda", "ppareuda", "neurida", "yeppeuda", "meositta", "jota",
    "nappeuda", "deopda", "chuul"
]

def HangulPort():
  Numero=randrange(0, 49)
  print(Hangul[Numero])
  resposta = input('Resposta:')
  if resposta==Portugues[Numero]:
    print('Certo')
    aawait=input('Proxima:')
    clear_output()
    HangulPort()
  else:
    print('Errou')
    print('Resposta correta:', Portugues[Numero])
    aawait=input('Proxima:')
    clear_output()
    HangulPort()

def HangulPort2():
  Numero=randrange(0, 99)
  print(Hangul2[Numero])
  resposta = input('Resposta:')
  if resposta==Portugues2[Numero]:
    print('Certo')
    aawait=input('Proxima:')
    clear_output()
    HangulPort2()
  else:
    print('Errou')
    print('Resposta correta:', Portugues2[Numero])
    aawait=input('Proxima:')
    clear_output()
    HangulPort2()

def HangulRom():
  Numero=randrange(0, 49)
  print(Hangul[Numero])
  resposta = input('Resposta:')
  if resposta==Romanizado[Numero]:
    print('Certo')
    aawait=input('Proxima:')
    clear_output()
    HangulRom()
  else:
    print('Errou')
    print('Resposta correta:', Romanizado[Numero])
    aawait=input('Proxima:')
    clear_output()
    HangulRom()

def HangulRom2():
  Numero=randrange(0, 99)
  print(Hangul2[Numero])
  resposta = input('Resposta:')
  if resposta==Romanizado2[Numero]:
    print('Certo')
    aawait=input('Proxima:')
    clear_output()
    HangulRom2()
  else:
    print('Errou')
    print('Resposta correta:', Romanizado2[Numero])
    aawait=input('Proxima:')
    clear_output()
    HangulRom2()

def RomPort():
  Numero=randrange(0, 49)
  print(Romanizado[Numero])
  resposta = input('Resposta:')
  if resposta==Portugues[Numero]:
    print('Certo')
    aawait=input('Proxima:')
    clear_output()
    RomPort()
  else:
    print('Errou')
    print('Resposta correta:', Portugues[Numero])
    aawait=input('Proxima:')
    clear_output()
    RomPort()

def RomPort2():
  Numero=randrange(0, 99)
  print(Romanizado2[Numero])
  resposta = input('Resposta:')
  if resposta==Portugues2[Numero]:
    print('Certo')
    aawait=input('Proxima:')
    clear_output()
    RomPort2()
  else:
    print('Errou')
    print('Resposta correta:', Portugues2[Numero])
    aawait=input('Proxima:')
    clear_output()
    RomPort2()

def Home():
  Opcao = input('Digite 1 se quer estudar Hangul-Português, digite 2 se quer estudar Hangul-Romanizado, digite 3 se quer estudar Romanizado-Português.\n')

  if Opcao=='1':
    print('Você quer estudar de Hangul para Português.\n')
    Dia = input('Digite 1 se quer estudar o dia 1, digite 2 se quer estudar o dia 2.\n')
    clear_output()
    if Dia=='1':
      HangulPort()
    if Dia=='2':
      HangulPort2()

    if Opcao=='2':
      print('Você quer estudar de Hangul para Romanizado.\n')
      Dia = input('Digite 1 se quer estudar o dia 1, digite 2 se quer estudar o dia 2.\n')
      clear_output()
    if Dia=='1':
      HangulRom()
    if Dia=='2':
      HangulRom2()

    if Opcao=='3':
      print('Você quer estudar de Romanizado para Português.\n')
      Dia = input('Digite 1 se quer estudar o dia 1, digite 2 se quer estudar o dia 2.\n')
      clear_output()
    if Dia=='1':
      RomPort()
    if Dia=='2':
      RomPort2()

Home()
