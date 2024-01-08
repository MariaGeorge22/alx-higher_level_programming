#include "lists.h"
/**
 * is_palindrome - linked list function
 * @head: start
 *
 * checks if list is a palindrome
 *
 * Return: 1 if true,
 * 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *middle = *head, *end = *head,
			  *old_next, *new_next = NULL, *current = *head;
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	old_next = *head;
	while (end != NULL && end->next != NULL)
	{
		middle = middle->next;
		end = end->next->next;
	}
	while (old_next != middle)
	{
		current = old_next;
		old_next = old_next->next;
		current->next = new_next;
		new_next = current;
	}
	if (end != NULL)
		middle = middle->next;
	while (current != NULL && middle != NULL)
	{
		if (current->n != middle->n)
			return (0);
		current = current->next;
		middle = middle->next;
	}
	return (1);
}
