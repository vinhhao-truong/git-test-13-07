class ListNode:
  def __init__(self, val: int) -> None:
    self.val = val
    self.next = None
    
class SinglyLinkedList:
  def __init__(self, val:int = None) -> None:
    self.head = None if val == None else ListNode(val)
    self.tail = None if val == None else ListNode(val)
  def __str__(self) -> str:
    pointer = self.head
    
    if pointer == None:
      return "[]"
    
    result = []
    
    while True:
      result.append(str(pointer.val))
      if pointer.next == None:
        break
      pointer = pointer.next
      
    return f'[{" -> ".join(result)}]'
    
  def insertHead(self, val:int):
    node = ListNode(val)
    node.next = self.head
    self.head = node
  def insertTail(self, val:int):
    node = ListNode(val)
    self.tail = node
    if self.head == None:
      self.head = node
      return
    
    pointer = self.head
    while pointer.next:
      pointer = pointer.next

    pointer.next = node
    
  def deleteHead(self):
    if self.head:
      self.head = self.head.next
      
  def deleteTail(self):
    pointer = self.head
    if pointer:
      if pointer.next:
        while pointer.next.next:
            pointer = pointer.next
        pointer.next = None
      self.tail = pointer
  
  def getNode(self, idx:int = 0):
    pointer = self.head
    count = 0
    if pointer:
      while count < idx and pointer.next:
        pointer = pointer.next
        count += 1
      if count < idx:
        return None
      return {
        "val": pointer.val,
        "next": pointer.next.val if pointer.next else None
      }
    else:
      return None
    
  
linked_list = SinglyLinkedList(1)
linked_list.insertHead(22)
linked_list.insertHead(25)
linked_list.insertHead(5)
linked_list.insertHead(215)
linked_list.insertTail(8)
linked_list.insertTail(17)

linked_list.deleteHead()
linked_list.deleteTail()
linked_list.deleteTail()


print(linked_list)
print(linked_list.getNode(-6))