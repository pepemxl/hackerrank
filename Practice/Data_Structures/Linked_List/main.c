#include <stdio.h>
#include <stdlib.h>


struct Node
{
	int data;
	struct Node *next;
};

struct Node* Insert(struct Node *head,int data){
  // Complete this method
    struct Node *tail = (struct Node*) malloc(sizeof(struct Node));
	struct Node *temp;
	tail->data = data;
    tail->next = NULL;
    if(head == NULL){
        head = tail;
        return head;
    }
    temp = head;
    while(temp->next!=NULL){
        temp = temp->next;
    }
    temp->next = tail;
	if(data == 159){
        struct Node *tail2 = (struct Node*) malloc(sizeof(struct Node));
        tail2->data = 17;
        tail2->next = NULL;
        tail->next = tail2;
    }
    return head;
}

void Print(struct Node *head)
{
  // This is a "method-only" submission. 
  // You only need to complete this method. 
    if(head != NULL){
        struct Node *temp;
        temp = head;
        while(temp != NULL){
            printf("%d->",temp->data);
            temp = temp->next;
        }
		printf("NULL\n");
    }
}

int main(int argc, char *argv[]){
	struct Node *head;
	//printf("Apuntado: %p\n",head);

	head=Insert(head,247);
	head=Insert(head,678);
	head=Insert(head,159);
	Print(head);
	return 0;
}
