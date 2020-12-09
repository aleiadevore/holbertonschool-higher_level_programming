#include "lists.h"

/**
 * makenode - makes a new node
 * @itr: node before new node
 * @number: value to store in new node
 * Return: pointer to node or NULL on failure
 */

listint_t *makenode(listint_t *itr, int number)
{
	listint_t *newnode, *tmp;

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	tmp = itr->next;
	itr->next = newnode;
	newnode->n = number;
	newnode->next = tmp;
	return (newnode);
}

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: head of linked list
 * @number: value to store in node
 * Return: pointer to new node or NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *itr, *nextnode;

	itr = *head;
	if (number <= itr->n)
	{
		newnode = makenode(*head, number);
		return (newnode);
	}
	for (itr = *head; itr != NULL; itr = itr->next)
	{
		nextnode = itr->next;
		if (number  > itr->n && nextnode == NULL)
		{
			newnode = makenode(itr, number);
			return (newnode);
		}
		else if (number > itr->n && number <= nextnode->n)
		{
			newnode = makenode(itr, number);
			return (newnode);
		}
	}
	return (NULL);
}
