#게임월드 모듈

#게임월드 표현
world = [ [], [] ]

#월드에 객체 담기
def add_object(o, depth=0):
    world[depth].append(o) # 지정된 깊이의 레이어에 객체 추가

#월드 객체들을 모두 업데이트
def update():
    for layer in world:
        for o in layer:
            o.update()

#월드 객체들을 모두 그리기
def render():
    for layer in world:
        for o in layer:
            o.draw()

#월드 객체 삭제
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('왜 없는걸 지우라 그래')






