#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *current = NULL, *next_node = NULL;
	listint_t *prev_slow = NULL, *mid = NULL, *next_slow  = NULL;
	int isPalindrome = 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		*next_slow = slow->next;
		slow->next = prev_slow;
		prev_slow = slow;
		slow = next_slow;
	}
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}
	else
	{
		mid = prev_slow;
	}
	while (mid != NULL && slow != NULL)
	{
		if (mid->data != slow->data)
		{
			isPalindrome = 0;
			break;
		}
		mid = mid->next, slow = slow->next;
	}
	current = prev_slow, prev_slow = NULL;
	while (current != NULL)
	{
		next_node = current->next;
		current->next = prev_slow;
		prev_slow = current;
		current = next_node;
	}
	return (isPalindrome);
}
