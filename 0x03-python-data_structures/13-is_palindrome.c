#include "lists.h"

/**
 * is_palindrome - determines if linked list is palindrome
 * @head: head of linked list
 * Return: 0 if not, 1 if is palindrome
 */

int is_palindrome(listint_t **head)
{
	int *name, i, j;
	listint_t *itr;

	if (*head == NULL)
		return (1);
	itr = *head;
	for (i = 0; itr != NULL; i++, itr = itr->next)
		;
	name = malloc(sizeof(int) * i);
	itr = *head;
	for (i = 0; itr != NULL; i++)
	{
		if (itr->n)
			name[i] = itr->n;
		itr = itr->next;
	}
	i--;
	for (j = 0; i > 0; j++, i--)
	{
		if (name[i] != name[j])
		{
			free(name);
			return (0);
		}
	}
	free(name);
	return (1);
}
