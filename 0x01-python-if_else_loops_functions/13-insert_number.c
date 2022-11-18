#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node -fnction.
 * Description: Function that inserts a number into a sorted singly linked list.
 * @head: double pointer of type listint_t
 * @number: number to be inserted in the list
 * Return: the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;
	listint_t *current;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
/*validate head is not null*/
	if (*head == NULL)
	{
		*head = newNode;
		newNode->next = NULL;
		return (newNode);
	}
	current = *head;
	while (current != NULL)
	{
		if ((number <= current->n))
		{
			newNode->next = current;
			*head = newNode;
			return (newNode);
		}
		if ((number >= current->n) && (current->next == NULL))
		{
			newNode->next = NULL;
			current->next = newNode;
			return (newNode);
		}
		if ((number >= current->n) && (number <= current->next->n))
		{
			newNode->next = current->next;
			current->next = newNode;
			return (newNode);
		}
		current = current->next;
	}
	return (NULL);
}
