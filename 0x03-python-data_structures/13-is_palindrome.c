#include "lists.h"

/**
 * is_palindrome - determines if linked list is palindrome
 * @head: head of linked list
 * Return: 0 if not, 1 if is palindrome
 */

int is_palindrome(listint_t **head)
{
	int name[100], val, i, j;
	listint_t *itr;

	if (*head == NULL)
		return (1);
	itr = *head;
	for (i = 0; itr != NULL; i++)
	{
		if (itr->n)
		{
			val = itr->n;
			name[i] = val;
		}
		itr = itr->next;
	}
	i--;
	for (j = 0; i > 0; j++, i--)
	{
		if (name[i] != name[j])
			return (0);
	}

	return (1);
}
