import lilypad as lily
import player
import item
import skills

def testStorage():
    lilypad = lily.Lilypad()

    # Fish Add
    assert lilypad.storageGetType("fish") == []
    assert lilypad.storageAdd(1,10) is True
    assert lilypad.storageGetType("fish")[0].getAmount() == 10
    assert lilypad.storageAdd(1,100) is True
    assert lilypad.storageGetType("fish")[0].getAmount() == 100

    # Fish Remove
    assert lilypad.storageRemove(1,50) is True
    assert lilypad.storageGetType("fish")[0].getAmount() == 50
    assert lilypad.storageRemove(1,50) is True
    assert lilypad.storageGetType("fish") == []

def testTools():
    lilypad = lily.Lilypad()

    # Adding Tool
    assert lilypad.getTools() == []
    assert lilypad.storageAdd(2,1)
    net = lilypad.storageFindId(2)
    assert lilypad.toolSet(net,0) is True
    assert lilypad.getTools()[0] == net

    # Changing tool
    assert lilypad.storageAdd(3,1)
    pole = lilypad.storageFindId(3)
    assert lilypad.toolSet(pole,0) is True
    assert lilypad.getStorage()[0] == net

def testFishing():
    lilypad = lily.Lilypad()
    frog = player.Player()

    # Fishing
    crew = lily.Crew('rocket')
    assert lilypad.crewAdd(crew) is True
    assert skills.fishing(frog,lilypad.getCrew()[0], lilypad) is False
    
    assert lilypad.storageAdd(2,1)
    tool = lilypad.storageFindId(2)
    
    rocket = lilypad.getCrew()[0]
    rocket.setJob('fishing')
    rocket.setTool(tool)

    assert skills.fishing(frog,lilypad.getCrew()[0], lilypad) is True
    assert len(lilypad.storageGetType("fish")) == 1